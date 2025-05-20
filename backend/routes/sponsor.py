from flask import request, jsonify, make_response, send_file
from app import app
from flask_security import auth_token_required, roles_accepted, verify_password, hash_password, current_user
from models import User, db, user_datastore, Campaign, Transactions, Ad, userreports, userratings, Campaignreports, Adrequest, Messages
from datetime import datetime
from Celery.tasks import add, createcsvcampaign, createcsvtransaction
from celery.result import AsyncResult

cache = app.cache

@app.route('/cache')

# Backend Jobs

# CSV Routes

# Create csv

@app.route('/createcsvcampaign')
@auth_token_required
@roles_accepted('Sponsor')
def createcsvcampaigns():
    task = createcsvcampaign.delay(current_user.id)
    return {'task_id': task.id}

@app.route('/createcsvtransaction')
@auth_token_required
@roles_accepted('Sponsor','Influencer','Admin')
def createcsvtransactions():
    task = createcsvtransaction.delay(current_user.id)
    return {'task_id': task.id}


# Send csv
@app.route('/getcampaigncsv/<task_id>')
def getcsv(task_id):
    task = AsyncResult(task_id)
    if task.ready():
        return send_file(f'./Celery/userdownloads/{task.result}'), 200
    else:
        return {'message': 'Task not ready'}, 202

@app.route('/getcsvtransaction/<task_id>')
def getcsvtransaction(task_id):
    task = AsyncResult(task_id)
    if task.ready():
        return send_file(f'./Celery/userdownloads/{task.result}'), 200
    else:
        return {'message': 'Task not ready'}, 202




# User Profile Routes

@app.route('/sponsorprofile/<int:id>', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer','Admin','Sponsor')
@cache.cached(timeout=50)
def sponsorprofile(id):
    if request.method == 'GET':
        user = User.query.get(id)
        if not user:
             return make_response(jsonify({"message":"User does not exist"}), 202)
        
        if user.current_login_at == None:
            return make_response(jsonify({'name':user.name,'id':user.id, 'username':user.username, 'email':user.email, 
                                      'role':user.roles[0].name, 'bio':user.bio, 'industry':user.personal_data['industry'],
                                      'site':user.personal_data['site'],'date_joined':datetime.strftime(user.date_joined, "%Y-%m-%d"), 
                                      'last_login':'Never', 'profilepic':user.personal_data['profpic']}), 200)
        else:
            return make_response(jsonify({'name':user.name,'id':user.id, 'username':user.username, 'email':user.email, 
                                      'role':user.roles[0].name, 'bio':user.bio, 'industry':user.personal_data['industry'],
                                      'site':user.personal_data['site'],'date_joined':datetime.strftime(user.date_joined, "%Y-%m-%d"), 
                                      'last_login':datetime.strftime(user.current_login_at, "%Y-%m-%d %H:%M"), 'profilepic':user.personal_data['profpic']}), 200)



# Edit Profile Route     
@app.route('/sponsorprofile/edit/<int:id>',methods=['GET','POST'])
@auth_token_required
@roles_accepted('Sponsor')
def sponsoreditprofile(id): 
    if request.method == 'POST':
            data = request.get_json()
            email = data.get('email')
            name = data.get('name')
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            is_terms = data.get('isterms')
            role = data.get('role')
            industry = data.get('industry')
            site = data.get('site')
            addinfo = data.get('addinfo')
            profpic = data.get('profpic')


            if is_terms != True:
                return make_response(jsonify({"message":"Please accept the terms and conditions"}), 202)
            
            
            if not email or not name or not username or not password or not confirm_password or not industry:
                return make_response(jsonify({"message":"Please enter data in all required fields"}), 202)
            
            if confirm_password != password:
                return make_response(jsonify({"message":"Passwords do not match"}),202)
            
            user = user_datastore.find_user(id=id)
            

            personal_data = {"industry":industry, "site":site, "addinfo":addinfo, "profpic":profpic, "theme":"Null"}
            hashed_password = hash_password(password)
            
            user.name = name
            user.username = username
            user.email = email
            user.password = hashed_password
            user.bio = addinfo
            user.personal_data = personal_data
            db.session.commit()
            return make_response(jsonify({"message":"Sponsor Profile Edited successfully"}),200)
            


# User Account Deletion Route   
@app.route('/sponsorprofile/deleteaccount/<int:id>', methods=['GET', 'POST','DELETE'])
@auth_token_required
@roles_accepted('Sponsor')
def sponsordelete(id):
    if request.method == 'POST':
        data = request.get_json()
        password = data.get('pass')
        user = User.query.get(id)
        if verify_password(password, user.password):
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({"message":"Account Deleted Successfully"}), 200)
        return make_response(jsonify({"message":"Incorrect Password"}), 202)
        

# Sponsor Dashboard Routes




# Campaign Routes

# Get Campaigns Route
@app.route('/sponsor/<int:id>/campaigns', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
@cache.cached(timeout=10)
def campaigns(id):
    if request.method == 'GET':
        sponsor = User.query.get(id)
        if not sponsor:
            return make_response(jsonify({'message':'Sponsor does not exist'}), 202)
        
        campaigns = sponsor.campaigns
        dataactive = []
        datainactive = []
        datacomplete = []
        for campaign in campaigns:
            if campaign.active == True and campaign.status != 'Completed':
                dataactive.append(campaign.formatter())
            elif campaign.active == False and campaign.status != 'Completed':
                datainactive.append(campaign.formatter())
            elif campaign.status == 'Completed':
                datacomplete.append(campaign.formatter())
            else:
                pass
        return make_response(jsonify({'activecampaigns':dataactive,'inactivecampaigns':datainactive, 'completedcampaigns':datacomplete }), 200)




# Create Campaign Route

@app.route('/sponsor/campaign', methods=['POST'])
@auth_token_required
@roles_accepted('Sponsor')
def campaign():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        desc = data.get('description')
        startdate = data.get('startdate')
        enddate = data.get('enddate')
        targetreach = data.get('target')
        goal= data.get('goal')
        visibility = data.get('accessType')
        budget = 0
        sponsor_id = current_user.id
        active = False
        industry = data.get('industry')
        niche = data.get('niche')
        
        if visibility == None or visibility == '':
            visibility = 'Private'

        if goal == None or goal == '':
            goal = 'No Specific Goal Set'
        
        if startdate == None or startdate == '':
            startdate = datetime.now()
        
        if enddate == None or enddate == '':
            return make_response(jsonify({'message':'Please enter an end date'}), 202)
        
        if startdate > enddate:
            return make_response(jsonify({'message':'Start date cannot be later than end date'}), 202)
        
        if startdate > datetime.now().strftime("%Y-%m-%d"):
            active = False

        if enddate < datetime.now().strftime("%Y-%m-%d"):
            active = False
        
        if startdate == datetime.now().strftime("%Y-%m-%d"):
            active = True

        if startdate < datetime.now().strftime("%Y-%m-%d"):
            return make_response(jsonify({'message':'Start date cannot be earlier than today'}), 202)
        

        if not current_user:
            return make_response(jsonify({'message':'User does not exist'}), 202)
        
        if not name or not desc or not startdate or not enddate or not targetreach or not visibility:
            return make_response(jsonify({'message':'Please enter data in all required fields'}), 202)
        
        try:
            start_date = datetime.strptime(startdate, '%Y-%m-%d') 
            end_date = datetime.strptime(enddate, '%Y-%m-%d')
        except:
            return make_response(jsonify({'message':'Invalid Date Format'}), 202)
        
        Status = 'Pending'

        new_campaign = Campaign(title=name, description=desc, start_date=start_date, status=Status ,end_date=end_date, budget=budget, sponsor_id=sponsor_id, target=targetreach, goal=goal, visibility=visibility, active=active, related_industry=industry, related_niche=niche)
        db.session.add(new_campaign)
        db.session.commit()
        return make_response(jsonify({'message':'Campaign Created Successfully'}), 200)
    

# Edit Campaign Route and Delete Campaign Route

@app.route('/sponsor/campaign/<int:id>', methods=['GET','PUT','POST'])
@auth_token_required
@roles_accepted('Sponsor')
def editdeletecampaign(id):
    if request.method == 'GET':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        return make_response(jsonify(campaign.formatter()), 200)
    
    if request.method == 'PUT':
        campaign = Campaign.query.get(id)
        data = request.get_json()
        name = data.get('name')
        desc = data.get('description')
        startdate = data.get('startdate')
        enddate = data.get('enddate')
        targetreach = data.get('target')
        goal= data.get('goal')
        visibility = data.get('accessType')
        budget = 0
        active = False
        industry = data.get('industry')
        niche = data.get('niche')
        
        if visibility == None or visibility == '':
            visibility = 'Private'

        if goal == None or goal == '':
            goal = 'No Specific Goal Set'
        
        if startdate == None or startdate == '':
            startdate = datetime.now()
        
        if enddate == None or enddate == '':
            return make_response(jsonify({'message':'Please enter an end date'}), 202)
        
        if startdate > enddate:
            return make_response(jsonify({'message':'Start date cannot be later than end date'}), 202)
        
        if startdate > datetime.now().strftime("%Y-%m-%d"):
            active = False

        if enddate < datetime.now().strftime("%Y-%m-%d"):
            active = False
        
        if startdate == datetime.now().strftime("%Y-%m-%d"):
            active = True

        
        if startdate < datetime.now().strftime("%Y-%m-%d"):
            return make_response(jsonify({'message':'Start date cannot be earlier than today'}), 202)

        if not current_user:
            return make_response(jsonify({'message':'User does not exist'}), 202)
        
        if not name or not desc or not startdate or not enddate or not targetreach or not visibility:
            return make_response(jsonify({'message':'Please enter data in all required fields'}), 202)
        
        try:
            start_date = datetime.strptime(startdate, '%Y-%m-%d') 
            end_date = datetime.strptime(enddate, '%Y-%m-%d')
        except:
            return make_response(jsonify({'message':'Invalid Date Format'}), 202)
        
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        campaign = Campaign.query.get(id)
        campaign.title = name
        campaign.description = desc
        campaign.start_date = start_date
        campaign.end_date = end_date
        campaign.target = targetreach
        campaign.goal = goal
        campaign.visibility = visibility
        campaign.related_industry = industry
        campaign.related_niche = niche
        campaign.active = active
        db.session.commit()
        return make_response(jsonify({'message':'Campaign Edited Successfully'}), 200)
    
    if request.method == 'POST':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        """ if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)"""
        data = request.get_json()
        password = data.get('pass')
        if not verify_password(password, current_user.password):
            return make_response(jsonify({'message':'Incorrect Password'}), 202)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        db.session.delete(campaign)
        db.session.commit()
        return make_response(jsonify({'message':'Campaign Deleted Successfully'}), 200)
    

# Campaign Activation Route

@app.route('/sponsor/campaign/<int:id>/activate', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def activatecampaign(id):
    if request.method == 'PUT':
        campaign = Campaign.query.get(id)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if campaign.active == True:
            return make_response(jsonify({'message':'Campaign is already active'}), 202)
        campaign.start_date = datetime.now()
        campaign.active = True
        db.session.commit()
        return make_response(jsonify({'message':'Campaign Activated Successfully'}), 200)

# Campaign Deactivation Route

@app.route('/sponsor/campaign/<int:id>/deactivate', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def deactivatecampaign(id):
    if request.method == 'PUT':
        campaign = Campaign.query.get(id)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if campaign.active == False:
            return make_response(jsonify({'message':'Campaign is already inactive'}), 202)
        campaign.active = False
        db.session.commit()
        return make_response(jsonify({'message':'Campaign Deactivated Successfully'}), 200)

# Campaign Completion Route

@app.route('/sponsor/campaign/<int:id>/complete', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def completecampaign(id):
    if request.method == 'PUT':
        campaign = Campaign.query.get(id)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if campaign.active == False:
            return make_response(jsonify({'message':'Campaign is inactive'}), 202)
        if campaign.budget < 0:
            return make_response(jsonify({'message':'Campaign Budget is in Negative Kindly Settle your Budget Bill To close the campaign'}), 202)
        campaign.status = 'Completed'
        campaign.end_date = datetime.now()
        campaign.active = False
        ads = campaign.ads
        for ad in ads:
            if ad.status != 'Completed' or ad.status != 'Approved' :
                ad.status = 'Closed'
        db.session.commit()
        return make_response(jsonify({'message':'Campaign Completed Successfully'}), 200)

# Adding Budget to Campaign Route
@app.route('/sponsor/campaign/<int:id>/addbudget', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def addbudget(id):
    if request.method == 'PUT':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        data = request.get_json()
        budget = data.get('budget')
        charge = data.get('charge')
        finalcharge = int(budget) + int(charge)
        if not charge:
            return make_response(jsonify({'message':'Please enter a charge amount'}), 202)
        if not budget:
            return make_response(jsonify({'message':'Please enter a budget amount'}), 202)
        campaign.budget += int(budget)
        user = User.query.get(1)
        user.wallet += charge
        Transaction_system = Transactions(transaction_type='Credit', amount=int(charge), user_id=1, date_created=datetime.now(), description='Budget Added to Campaign '+campaign.title+' by Sponsor '+ current_user.name)
        Transaction_user = Transactions(transaction_type='Credit', amount=int(finalcharge), user_id=current_user.id, date_created=datetime.now(),description='Budget Added to Campaign '+campaign.title)
        db.session.add(Transaction_system)
        db.session.add(Transaction_user)
        db.session.commit()
        return make_response(jsonify({'message':'Budget Added Successfully'}), 200)

# View Transactions Route

@app.route('/sponsor/wallet', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
@cache.cached(timeout=30)
def transactions():
    if request.method == 'GET':
        transactions = Transactions.query.filter_by(user_id=current_user.id).all()
        data = []
        for transaction in transactions:
            data.append(transaction.formatter())
        return make_response(jsonify(data), 200)



# Campaign View Route

@app.route('/sponsor/campaign/<int:id>/view', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor','Influencer','Admin')
def viewcampaign(id):
    if request.method == 'GET':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        return make_response(jsonify(campaign.formatter()), 200)

# Campaign Public View
@app.route('/campaign/<int:id>/publicview', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor','Influencer','Admin')
def publicviewcampaign(id):
    if request.method == 'GET':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        return make_response(jsonify(campaign.formatter()), 200)


# Create Ad Route

@app.route('/sponsor/campaign/<int:id>/createad', methods=['POST'])
@auth_token_required
@roles_accepted('Sponsor')
def createad(id):
    if request.method == 'POST':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed so Ad cannot be created'}), 202)
        data = request.get_json()
        title = data.get('title')
        desc = data.get('description')
        adamount = data.get('amount')
        adplatforms = data.get('platforms')
        adstatus = 'Open'
        if int(adamount)>campaign.budget:
            return make_response(jsonify({'message':'Ad amount cannot be greater than current campaign budget'}), 202)
        if not title or not desc or not adamount or not adplatforms:
            return make_response(jsonify({'message':'Please enter data in all required fields'}), 202)
        negociatedprice = int(adamount)
        new_ad = Ad(title=title, description=desc, baseprice=int(adamount), negociatedprice=negociatedprice, preferedplatforms=adplatforms,status=adstatus, campaign_id=campaign.id)
        db.session.add(new_ad)
        db.session.commit()
        return make_response(jsonify({'message':'Ad Created Successfully'}), 200)

# Get All Ads Route

@app.route('/campaign/<int:id>/ads', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor','Influencer','Admin')
def ads(id):
    if request.method == 'GET':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        ads = campaign.ads
        data = []
        for ad in ads:
            data.append(ad.formatter())
        return make_response(jsonify(data), 200)

# Edit Ad Route

@app.route('/ad/<int:id>/edit', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def editad(id):
    if request.method == 'PUT':
        ad = Ad.query.get(id)
        campaigned = Campaign.query.get(ad.campaign_id)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        if campaigned.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed so Ad cannot be Edited'}), 202)
        data = request.get_json()
        title = data.get('title')
        desc = data.get('description')
        adamount = data.get('amount')
        adplatforms = data.get('platforms')
        
        if not title or not desc or not adamount or not adplatforms:
            return make_response(jsonify({'message':'Please enter data in all required fields'}), 202)
        if int(adamount)>campaigned.budget:
            return make_response(jsonify({'message':'Ad amount cannot be greater than current campaign budget'}), 202)
        ad.title = title
        ad.description = desc
        ad.baseprice = int(adamount)
        ad.negociatedprice = int(adamount)
        ad.preferedplatforms = adplatforms
        ad.negociatedprice = int(adamount)
        db.session.commit()
        return make_response(jsonify({'message':'Ad Edited Successfully'}), 200)

# Delete Ad Route

@app.route('/ad/<int:id>/delete', methods=['DELETE'])
@auth_token_required
@roles_accepted('Sponsor')
def deletead(id):
    if request.method == 'DELETE':
        ad = Ad.query.get(id)
        campaigned = Campaign.query.get(ad.campaign_id)
        if campaigned.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed so Ad cannot be Deleted'}), 202)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        db.session.delete(ad)
        db.session.commit()
        return make_response(jsonify({'message':'Ad Deleted Successfully'}), 200)

# Report Sponsor Route

@app.route('/sponsor/<int:id>/report', methods=['POST'])
@auth_token_required
@roles_accepted('Influencer','Admin')
def reportsponsor(id):
    if request.method == 'POST':
        data = request.get_json()
        report = data.get('issue')
        detail = data.get('details')
        reason = data.get('reason')
        user = User.query.get(id)
        user.reported += 1
        if not report:
            return make_response(jsonify({'message':'Please enter a Issue'}), 202)
        if not detail:
            return make_response(jsonify({'message':'Please enter a detail'}), 202)
        if not reason:
            return make_response(jsonify({'message':'Please enter a reason'}), 202)
        new_report = userreports(user_id=id, issue=report, description=detail, issuecategory=reason, date_created=datetime.now(), submitted_by=current_user.username)
        db.session.add(new_report)
        db.session.commit()
        return make_response(jsonify({'message':'Report Submitted Successfully'}), 200)

# Report Campaign Route

@app.route('/campaign/<int:id>/report', methods=['POST'])
@auth_token_required
@roles_accepted('Influencer','Admin')
def reportcampaign(id):
    if request.method == 'POST':
        data = request.get_json()
        report = data.get('issue')
        detail = data.get('details')
        reason = data.get('reason')
        campaign = Campaign.query.get(id)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed so it cannot be reported'}), 202)
        if not report:
            return make_response(jsonify({'message':'Please enter a Issue'}), 202)
        if not detail:
            return make_response(jsonify({'message':'Please enter a detail'}), 202)
        if not reason:
            return make_response(jsonify({'message':'Please enter a reason'}), 202)
        new_report = Campaignreports(campaign_id=id, issue=report, description=detail, issuecategory=reason, date_created=datetime.now(), submitted_by=current_user.username)
        db.session.add(new_report)
        db.session.commit()
        return make_response(jsonify({'message':'Report Submitted Successfully'}), 200)
    

# Sponsor Statistics Route

@app.route('/sponsor/<int:id>/statistics', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
def statistics(id):
    if request.method == 'GET':
        sponsor = User.query.get(id)
        campaign = sponsor.campaigns
        totalcampaigns = len(campaign)
        totalads = 0
        totalamount = 0
        completedcampaigns = 0
        flaggedcampaigns = 0
        publiccampaigns = 0
        privatecampaigns = 0
        activecampaigns = 0
        inactivecampaigns = 0

        adcompleted = 0
        adopen = 0
        adclosed = 0
        adapproved = 0
        adrejected = 0
        adpending = 0
        adrequested = 0
        adnegociated = 0
        adcompleted = 0
        adinprogress = 0

        for camp in campaign:
            ads = camp.ads
            for ad in ads:
                totalads += 1
                if ad.status == 'Open':
                    adopen += 1
                if ad.status == 'Closed':
                    adclosed += 1
                if ad.status == 'Approved':
                    adapproved += 1
                if ad.status == 'Rejected':
                    adrejected += 1
                if ad.status == 'Pending':
                    adpending += 1
                if ad.status == 'Requested':
                    adrequested += 1
                if ad.status == 'Negociated':
                    adnegociated += 1
                if ad.status == 'Completed':
                    adcompleted += 1
                if ad.status == 'In Progress':
                    adinprogress += 1

            if camp.status == 'Completed':
                completedcampaigns += 1
            if camp.status == 'Flagged':
                flaggedcampaigns += 1
            if camp.visibility == 'Public':
                publiccampaigns += 1
            if camp.visibility == 'Private':
                privatecampaigns += 1
            if camp.active == True:
                activecampaigns += 1
            if camp.active == False:
                inactivecampaigns += 1
        transactions = Transactions.query.filter_by(user_id=id).all()
        for transaction in transactions:
            totalamount += transaction.amount
        if not sponsor:
            return make_response(jsonify({'message':'Sponsor does not exist'}), 202)
        
        return make_response(jsonify({'totalcampaigns':totalcampaigns, 'totalads':totalads, 'totalamount':totalamount, 
                                      'completedcampaigns':completedcampaigns, 'flaggedcampaigns':flaggedcampaigns, 'publiccampaigns':publiccampaigns, 
                                      'privatecampaigns':privatecampaigns, 'activecampaigns':activecampaigns, 'inactivecampaigns':inactivecampaigns,
                                      'adopen':adopen, 'adclosed':adclosed, 'adapproved':adapproved, 'adrejected':adrejected, 'adpending':adpending,
                                      'adrequested':adrequested, 'adnegociated':adnegociated, 'adcompleted':adcompleted, 'adinprogress':adinprogress}), 200)

# Sponsor home route

@app.route('/sponsor/home', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
@cache.cached(timeout=30)
def sponsorhome():
     if request.method == 'GET':
        flag = current_user.flagged
        users = User.query.filter_by().all()
        data = []
        for user in users:
             if user.roles[0].name == 'Influencer' and user.active == 1 and user.flagged==0:
                 data.append(user.formatteruserinfluencer())
        return make_response(jsonify({'data':data,'flag':flag}), 200)


# Sponsor Hire Influencer get route

@app.route('/sponsor/<int:id>/hireinfluencer', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
def sponsorhireinfluencer(id):
    if request.method == 'GET':
        campaigns = Campaign.query.get(id)
        if not campaigns:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        industry = campaigns.related_industry
        industry = industry.lower()

        users = User.query.filter_by().all()
        data = []
        for user in users:
            if user.roles[0].name == 'Influencer' and user.active == 1 and user.flagged==0 and user.personal_data['industry'].lower() == industry:
                data.append(user.formatteruserinfluencer())
        return make_response(jsonify(data), 200)
    
# Sponsor Hire Influencer post route

@app.route('/sponsor/<int:id>/hireinfluencer/<int:influid>', methods=['POST'])
@auth_token_required
@roles_accepted('Sponsor')
def sponsorhireinfluencerpost(id,influid):
    if request.method == 'POST':
            influencer = User.query.get(influid)
            ad = Ad.query.get(id)
            if not influencer:
                return make_response(jsonify({'message':'Influencer does not exist'}), 202)
            if not ad:
                return make_response(jsonify({'message':'Ad does not exist'}), 202)
            if ad.status == 'Closed':
                return make_response(jsonify({'message':'Ad is closed'}), 202)
            if ad.status == 'Completed':
                return make_response(jsonify({'message':'Ad is completed'}), 202)
            
            if ad.status == 'Approved':
                return make_response(jsonify({'message':'Ad is already approved'}), 202)
            
            new_adrequest = Adrequest(ad_id=id, user_id=influid, date_created=datetime.now(), status='Requested', negociatedprice=ad.baseprice, requested_bysponsor=True)
            ad.status = 'Requested'
            db.session.add(new_adrequest)
            db.session.commit()
            return make_response(jsonify({'message':'Ad Request Sent Successfully'}), 200)

# Ad Requests Routes

@app.route('/sponsor/<int:id>/adrequests', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
@cache.cached(timeout=10)
def adrequests(id):
    if request.method == 'GET':
        campaigns = Campaign.query.filter_by(sponsor_id=id).all()
        dataapprove = []
        datarequest = []
        datacomplete = []
        datareject = []
        for campaign in campaigns:
            ads = campaign.ads 
            for ad in ads:
                adrequests = ad.adrequested
                for adrequest in adrequests:
                    if adrequest.status == 'Requested' or adrequest.status == 'Negociated':
                        datarequest.append(adrequest.formatter())
                    if adrequest.wasapproved == True and adrequest.status == 'InProgress':
                        dataapprove.append(adrequest.formatter())
                    if adrequest.status == 'Completed':
                        datacomplete.append(adrequest.formatter())
                    if adrequest.status == 'Rejected':
                        datareject.append(adrequest.formatter())
                    
        
        return make_response(jsonify({'requests':datarequest,'approved':dataapprove,'completed':datacomplete,'rejected':datareject}), 200)

# Ad Request Removal Route

@app.route('/adrequest/<int:id>/remove', methods=['DELETE'])
@auth_token_required
@roles_accepted('Sponsor')
def removeadrequest(id):
    if request.method == 'DELETE':
        adrequest = Adrequest.query.get(id)
        ad = Ad.query.get(adrequest.ad_id)
        campaign = Campaign.query.get(ad.campaign_id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        ad = Ad.query.get(adrequest.ad_id)
        if ad.status == 'Closed':
            return make_response(jsonify({'message':'Ad is closed'}), 202)
        if ad.status == 'Completed':
            return make_response(jsonify({'message':'Ad is completed'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is completed'}), 202)
        if adrequest.wasapproved == True:
            return make_response(jsonify({'message':'Ad Request is already approved'}), 202)
        
        if campaign.status == 'Completed':
            ad.status = 'Closed'
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        if campaign.status == 'Pending':
            ad.status = 'Open'
        
        if adrequest.requested_bysponsor == True:
            ad.status = 'Open'

        db.session.delete(adrequest)
        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Removed Successfully'}), 200)


# Ad Request Approval Route

@app.route('/adrequest/<int:id>/approve', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def approveadrequest(id):
    if request.method == 'PUT':
        adrequest = Adrequest.query.get(id)
        ad = Ad.query.get(adrequest.ad_id)
        campaign = Campaign.query.get(ad.campaign_id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if ad.status == 'Closed':
            return make_response(jsonify({'message':'Ad is closed'}), 202)
        if ad.status == 'Completed':
            return make_response(jsonify({'message':'Ad is completed'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is completed'}), 202)
        if adrequest.wasapproved == True:
            return make_response(jsonify({'message':'Ad Request is already approved'}), 202)
        
        if campaign.status == 'Completed':
            ad.status = 'Closed'
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        if campaign.status == 'Pending':
            ad.status = 'Approved'
        
        if adrequest.requested_bysponsor == True:
            ad.status = 'Approved'
        
        adrequest.wasapproved = True
        adrequest.status = 'InProgress'
        adrequest.granted_at = datetime.now()
        adrequest.finish_by = campaign.end_date 
        ad.negociatedprice = adrequest.negociatedprice
        campaign.budget -= adrequest.negociatedprice
        user = User.query.get(adrequest.user_id)
        user.wallet += adrequest.negociatedprice
        user = User.query.get(adrequest.user_id)
        transaction1 = Transactions(user_id=adrequest.user_id, amount=adrequest.negociatedprice, date_created=datetime.now(), transaction_type='Credit', description='Ad Request Accepted for Ad '+str(ad.title)+' under Campaign '+campaign.title+' by Sponsor '+current_user.name)
        transaction2 = Transactions(user_id=current_user.id, amount=adrequest.negociatedprice, date_created=datetime.now(), transaction_type='Debit', description='Ad Request Accepted for Ad '+str(ad.title)+' under Campaign '+campaign.title+' by Influencer '+user.username)

        db.session.add(transaction1)
        db.session.add(transaction2)

        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Approved Successfully'}), 200)

# Ad Request Rejection Route

@app.route('/adrequest/<int:id>/reject', methods=['PUT'])
@auth_token_required
@roles_accepted('Sponsor')
def rejectadrequest(id):
    if request.method == 'PUT':
        adrequest = Adrequest.query.get(id)
        ad = Ad.query.get(adrequest.ad_id)
        campaign = Campaign.query.get(ad.campaign_id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if ad.status == 'Closed':
            return make_response(jsonify({'message':'Ad is closed'}), 202)
        if ad.status == 'Completed':
            return make_response(jsonify({'message':'Ad is completed'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is completed'}), 202)
        if adrequest.wasapproved == True:
            return make_response(jsonify({'message':'Ad Request is already approved'}), 202)
        
        if campaign.status == 'Completed':
            ad.status = 'Closed'
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        
        if campaign.status == 'Pending':
            ad.status = 'Open'
        
        if adrequest.requested_bysponsor == True:
            ad.status = 'Open'
        
        ad.status = 'Open'
        ad.negociatedprice = ad.baseprice
        adrequest.wasapproved = False
        adrequest.status = 'Rejected'
        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Rejected Successfully'}), 200)


# Rate Influencer Route

@app.route('/sponsor/rateinfluencer', methods=['POST'])
@auth_token_required
@roles_accepted('Sponsor')
def rateinfluencer():
    if request.method == 'POST':
        data = request.get_json()
        influencer_id = data.get('influencer_id')
        rating = data.get('rating')
        review = data.get('review')
        if not influencer_id:
            return make_response(jsonify({'message':'Please enter Influencer ID'}), 202)
        if not rating:
            return make_response(jsonify({'message':'Please enter a Rating'}), 202)
        if not review:
            return make_response(jsonify({'message':'Please enter a Review'}), 202)
        influencer = User.query.get(influencer_id)
        if not influencer:
            return make_response(jsonify({'message':'Influencer does not exist'}), 202)
        new_rating = userratings(user_id=influencer_id, rating=rating, review=review, date_created=datetime.now(), submitted_by=current_user.username)
        db.session.add(new_rating)
        db.session.commit()

        reviews = userratings.query.filter_by(user_id=influencer_id).all()
        totalrating = 0
        for review in reviews:
            totalrating += review.rating
        influencer.avgrating = totalrating/len(reviews)
        db.session.commit()
        return make_response(jsonify({'message':'Influencer Rated Successfully'}), 200)

# Get all ads route

@app.route('/sponsor/ads', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor')
def allads():
    if request.method == 'GET':
        campaign = Campaign.query.filter_by(sponsor_id=current_user.id).all()
        data = []
        for camp in campaign:
            ads = Ad.query.filter_by(campaign_id=camp.id).all()
            for ad in ads:
                if ad.status == 'Open':
                    data.append(ad.formatter())
        
        return make_response(jsonify(data), 200)
    
# Chat with Influencer Route

# get all and send message chats route

@app.route('/sponsor/<int:id>/chats', methods=['GET','POST'])
@auth_token_required
@roles_accepted('Sponsor')
def allchats(id):
    if request.method == 'GET':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request has been completed'}), 202)
        if adrequest.status == 'Rejected':
            return make_response(jsonify({'message':'Ad Request has been rejected'}), 202)
        chats = Messages.query.filter_by(request_id=id).all()
        data = []
        for chat in chats:
            data.append(chat.formatter())
        return make_response(jsonify(data), 200)
    
    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message')
        requesteduser =Adrequest.query.get(id)
        receiver = requesteduser.user_id
        if not message:
            return make_response(jsonify({'message':'Please enter a message'}), 202)
        new_message = Messages(request_id=id, message=message, date_created=datetime.now(), sender=current_user.id, receiver=receiver )
        db.session.add(new_message)
        db.session.commit()
        return make_response(jsonify({'message':'Message Sent Successfully'}), 200)

# Get Ad from Ad request route

@app.route('/adrequest/<int:id>/ad', methods=['GET'])
@auth_token_required
@roles_accepted('Sponsor','Influencer')
def getadfromrequest(id):
    if request.method == 'GET':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        ad = Ad.query.get(adrequest.ad_id)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        return make_response(jsonify(ad.formatter()), 200)

# Get negociation from Ad request route

@app.route('/adrequest/<int:id>/negociation', methods=['POST'])
@auth_token_required
@roles_accepted('Sponsor','Influencer')
def getnegociationfromrequest(id):
    if request.method == 'POST':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        ad = Ad.query.get(adrequest.ad_id)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        data = request.get_json()
        price = data.get('price')
        if not price:
            return make_response(jsonify({'message':'Please enter a price'}), 202)
        adrequest.negociatedprice = price
        adrequest.status = 'Negociated'
        ad.isnegociated = True
        ad.negociatedprice = price
        db.session.commit()
        return make_response(jsonify({'message':'Negociation Sent Successfully'}), 200)
    