from flask import request, jsonify, make_response
from app import app
from flask_security import auth_token_required, roles_accepted, verify_password, hash_password, current_user
from models import User, db, user_datastore, Transactions, userreports, userratings, Campaignreports, Campaign, Ad, Adrequest, Messages
from datetime import datetime

cache = app.cache

def wordtotalreach(totalreach):
            if totalreach >= 1000000000: 
                totalreach = f'{totalreach / 1000000000:.1f} B' 
            elif totalreach >= 1000000: 
                if totalreach >= 10000000: # Handle up to 100M 
                    totalreach = f'{totalreach / 1000000:.0f} M' 
                else: 
                    totalreach = f'{totalreach / 1000000:.1f} M' 
            elif totalreach >= 1000: 
                if totalreach >= 10000: # Handle up to 100K 
                    totalreach = f'{totalreach / 1000:.0f} K' 
                else: 
                    totalreach = f'{totalreach / 1000:.1f} K' 
            else: 
                totalreach = str(totalreach)
            return totalreach 

def wordtotalreachs(totalreach):
            if totalreach >= 1000000000: 
                totalreach = f'{totalreach / 1000000000:.1f} Billion' 
            elif totalreach >= 1000000: 
                if totalreach >= 10000000: # Handle up to 100M 
                    totalreach = f'{totalreach / 1000000:.0f} Million' 
                else: 
                    totalreach = f'{totalreach / 1000000:.1f} Million' 
            elif totalreach >= 1000: 
                if totalreach >= 10000: # Handle up to 100K 
                    totalreach = f'{totalreach / 1000:.0f} Thousand' 
                else: 
                    totalreach = f'{totalreach / 1000:.1f} Thousand' 
            else: 
                totalreach = str(totalreach)
            return totalreach 

# User Profile Routes

@app.route('/influencerprofile/<int:id>', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer','Admin','Sponsor')
@cache.cached(timeout=40)
def influencerprofile(id):
    if request.method == 'GET':
        user = User.query.get(id)
    info = user.personal_data
    totalreach = 0
    if user.current_login_at:
        data = {'name':user.name,'id':user.id, 'rating':user.avgrating ,'username':user.username, 'profilepic':user.personal_data['profpic'],'email':user.email, 'bio':user.bio, 'industry':info['industry'], 'theme':info['theme'], 'niche':info['niche']  ,'date_joined':datetime.strftime(user.date_joined, "%Y-%m-%d"), 'last_login':datetime.strftime(user.current_login_at, "%Y-%m-%d %H:%M")}
    else:
        data = {'name':user.name,'id':user.id,'rating':user.avgrating  ,'username':user.username, 'profilepic':user.personal_data['profpic'],'email':user.email, 'bio':user.bio, 'industry':info['industry'], 'theme':info['theme'], 'niche':info['niche']  ,'date_joined':datetime.strftime(user.date_joined, "%Y-%m-%d"), 'last_login':'Not Logged In Yet'}
    
    for i in info['social_media']:
        data[i]=info['social_media'][i][0]
        if(info['social_media'][i][0]==True):
            data[i+'followers']=wordtotalreach(int(info['social_media'][i][1]))
            totalreach += int(info['social_media'][i][1])
        data[i+'link']=info['social_media'][i][2]
    
    
    data['totalreach']=wordtotalreachs(totalreach)
    
    
    if not user:
             return make_response(jsonify({"message":"User does not exist"}), 202)
    return make_response(jsonify(data), 200)


# Edit Profile Route     
@app.route('/editinfluencerprofile/<int:id>',methods=['GET','POST'])
@auth_token_required
@roles_accepted('Influencer')
def influencereditprofile(id): 
    if request.method == 'POST':
            
            user=User.query.get(id)

            data = request.get_json()
            email = data.get('email')
            name = data.get('name')
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            is_terms = data.get('isterms')
            role = data.get('role')
            addinfo = data.get('addinfo')
            profpic = data.get('haveprofile')
            industry = data.get('industry')
            niche = data.get('niche')
            isyt = data.get('isyt')
            isfb = data.get('isfb')
            isinsta = data.get('isinsta')
            islinkedin = data.get('islinked')
            isthread = data.get('isthread')
            istiktok = data.get('istik')
            iskick = data.get('iskick')
            istwitch = data.get('istwitch')
            istwitter = data.get('isx')
            issnap = data.get('issnap')

            personal_data = { "industry":industry, "Addinfo":addinfo, "profpic":profpic, "theme":"Null", "niche":niche,"social_media": {"youtube":[isyt,data.get("ytfollowers"),data.get("ytlink")], 
                            "facebook":[isfb,data.get("fbfollowers"),data.get("fblink")], "instagram":[isinsta,data.get("instafollowers"),data.get("instalink")],
                            "linkedin":[islinkedin,data.get("linkedfollowers"),data.get("linkedlink")], "tiktok":[istiktok,data.get("tikfollowers"),data.get("tiklink")],
                            "twitter":[istwitter,data.get("xfollowers"),data.get("xlink")], "snapchat":[issnap,data.get("snapfollowers"),data.get("snaplink")],
                            "twitch":[istwitch,data.get("twitchfollowers"),data.get("twitchlink")], "kick":[iskick,data.get("kickfollowers"),data.get("kicklink")],
                            "thread":[isthread,data.get("threadfollowers"),data.get("threadlink")]
                            },}
            
            if is_terms != True:
                return make_response(jsonify({"message":"Please accept the terms and conditions"}), 202)

            if not email or not name or not username or not password or not confirm_password:
                return make_response(jsonify({"message":"Please enter data in all required fields"}), 202)
            
            if confirm_password != password:
                return make_response(jsonify({"message":"Passwords do not match"}),202)
            
            if not isyt and not isfb and not isinsta and not islinkedin and not isthread and not istiktok and not iskick and not istwitch and not istwitter and not issnap:
                return make_response(jsonify({"message":"Please select atleast one social media platform"}),202)

            user1 = user_datastore.find_user(username=username)

            if user1:
                return make_response(jsonify({"message":"User already exists Kindly Choose other username"}),202)
        
            if username != user.username:
                new_username = User.query.filter_by(username=username).first()

            if new_username:
                return make_response(jsonify({"message":"Username already exists"}), 202)
    
        
            new_password_hashed = hash_password(password)
            user.username = username
            user.password = new_password_hashed
            user.name = name
            user.bio = addinfo
            user.email = email
            user.personal_data = personal_data

            db.session.commit()
            return make_response(jsonify({"message":"Profile Updated Successfully"}), 200)


# User Account Deletion Route   
@app.route('/influencerprofile/deleteaccount/<int:id>', methods=['GET', 'POST','DELETE'])
@auth_token_required
@roles_accepted('Influencer')
def influencerdelete(id):
    if request.method == 'POST':
        data = request.get_json()
        password = data.get('pass')
        user = User.query.get(id)
        if verify_password(password, user.password):
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({"message":"Account Deleted Successfully"}), 200)
        else:
            return make_response(jsonify({"message":"Incorrect Password"}), 202)
    return make_response(jsonify({"message":"Unknown Error Occured"}), 202)

# Influencer wallet routes

@app.route('/influencer/wallet', methods=['GET'])  
@auth_token_required
@roles_accepted('Influencer')
@cache.cached(timeout=30)
def influencerwallet():
    if request.method == 'GET':
            transactions = Transactions.query.filter_by(user_id=current_user.id).all()
            data = []
            for transaction in transactions:
                data.append(transaction.formatter())
            response = {'transactions':data, 'balance':current_user.wallet}
            return make_response(jsonify(response), 200)     


# Report Influencer Route

@app.route('/influencer/<int:id>/report', methods=['POST'])
@auth_token_required
@roles_accepted('Sponsor','Admin')
def reportinfluencer(id):
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

# Get All Public Campaigns

@app.route('/influencer/home', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer')
@cache.cached(timeout=30)
def influencercampaigns():
    if request.method == 'GET':
        campaigns = Campaign.query.filter_by(visibility='Public', status='Pending',active=True).all()
        data = []
        for campaign in campaigns:
            data.append(campaign.formatter())
        return make_response(jsonify({'data':data,'flag':current_user.flagged}), 200)


# Apply for Ad request

@app.route('/campaign/<int:id1>/applyadrequest/<int:id2>', methods=['POST'])
@auth_token_required
@roles_accepted('Influencer')
def applyadrequest(id1,id2):
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.get(current_user.id)
        campaign = Campaign.query.get(id1)
        ad = Ad.query.get(id2)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if not campaign.active:
            return make_response(jsonify({'message':'Campaign is not active'}), 202)
        if not campaign.status == 'Pending':
            return make_response(jsonify({'message':'Campaign is not accepting applications'}), 202)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        if ad.status == 'Closed':
            return make_response(jsonify({'message':'Ad is closed'}), 202)
        
        price = ad.baseprice
        
        if ad.status == 'Open':
            new_adrequest = Adrequest(user_id=user.id,  ad_id=ad.id, date_created=datetime.now(), status='Requested', requested_byinfluencer=True, negociatedprice=price)
            ad.status = 'Requested'
            db.session.add(new_adrequest)
        
       
        db.session.commit()
        return make_response(jsonify({'message':'Application Submitted Successfully'}), 200)

# Get All Ad Requests

@app.route('/influencer/<int:id>/adrequests', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer')
@cache.cached(timeout=30)
def influenceradrequests(id):
    if request.method == 'GET':
        adrequests = Adrequest.query.filter_by(user_id=id).all()
        datacomp = []
        datareq = []
        dataapproved = []
        datarejected = []
        for adrequest in adrequests:
            if adrequest.status == 'Completed':
                datacomp.append(adrequest.formatter())
            elif adrequest.status == 'Requested' or adrequest.status == 'Negociated':
                datareq.append(adrequest.formatter())
            elif adrequest.wasapproved == True:
                dataapproved.append(adrequest.formatter())
            elif adrequest.status == 'Rejected':
                datarejected.append(adrequest.formatter())
      
        return make_response(jsonify({ 'datacomp':datacomp, 'datareq':datareq, 'datareject':datarejected, 'dataapprove':dataapproved }), 200)

# Accept Ad Request

@app.route('/influencer/adrequest/<int:id>/accept', methods=['PUT'])
@auth_token_required
@roles_accepted('Influencer')
def acceptadrequest(id):
    if request.method == 'PUT':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is already completed'}), 202)
        if adrequest.status == 'Rejected':
            return make_response(jsonify({'message':'Ad Request is already rejected'}), 202)
        if adrequest.wasapproved == True:
            return make_response(jsonify({'message':'Ad Request is already approved'}), 202)
        adrequest.wasapproved = True
        adrequest.status = 'InProgress'
        ad = Ad.query.get(adrequest.ad_id)
        campaign = Campaign.query.get(ad.campaign_id)
        ad.negociatedprice = adrequest.negociatedprice
        transaction1 = Transactions(user_id=adrequest.user_id, amount=adrequest.negociatedprice, date_created=datetime.now(), transaction_type='Credit', description='Ad Request Accepted for Ad '+str(ad.title)+' under Campaign '+campaign.title)
        transaction2 = Transactions(user_id=campaign.sponsor_id, amount=adrequest.negociatedprice, date_created=datetime.now(), transaction_type='Debit', description='Ad Request Accepted for Ad '+str(ad.title)+' under Campaign '+campaign.title+' by Influencer '+current_user.username)
        current_user.wallet += adrequest.negociatedprice
        adrequest.granted_at = datetime.now()
        adrequest.finish_by = campaign.end_date
        campaign.budget -= adrequest.negociatedprice
        ad.status = "Approved"
        db.session.add(transaction1)
        db.session.add(transaction2)
        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Approved Successfully'}), 200)


# Reject Ad Request

@app.route('/influencer/adrequest/<int:id>/reject', methods=['PUT'])
@auth_token_required
@roles_accepted('Influencer')
def influencerrejectadrequest(id):
    if request.method == 'PUT':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is already completed'}), 202)
        if adrequest.status == 'Rejected':
            return make_response(jsonify({'message':'Ad Request is already rejected'}), 202)
        if adrequest.wasapproved == True:
            return make_response(jsonify({'message':'Ad Request is already approved'}), 202)
        adrequest.status = 'Rejected'
        ad = Ad.query.get(adrequest.ad_id)
        ad.status = 'Open'
        ad.negociatedprice = ad.baseprice
        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Rejected Successfully'}), 200)

# Complete Ad Request

@app.route('/influencer/adrequest/<int:id>/complete', methods=['PUT'])
@auth_token_required
@roles_accepted('Influencer')
def completeadrequest(id):
    if request.method == 'PUT':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is already completed'}), 202)
        if adrequest.status == 'Rejected':
            return make_response(jsonify({'message':'Ad Request is already rejected'}), 202)
        if adrequest.wasapproved == False:
            return make_response(jsonify({'message':'Ad Request is not approved'}), 202)
        adrequest.status = 'Completed'
        ad = Ad.query.get(adrequest.ad_id)
        campaign = Campaign.query.get(ad.campaign_id)
        campaign.current += current_user.totalfollowers
        campaign.progress = (campaign.current/campaign.target)*100
        if campaign.current >= campaign.target:
            campaign.progress = 100
        ad.status = 'Completed'
        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Completed Successfully'}), 200)

# Remove Ad Request

@app.route('/influencer/adrequest/<int:id>/remove', methods=['DELETE'])
@auth_token_required
@roles_accepted('Influencer')
def influencerremoveadrequest(id):
    if request.method == 'DELETE':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is already completed'}), 202)
        if adrequest.status == 'Rejected':
            return make_response(jsonify({'message':'Ad Request is already rejected'}), 202)
        if adrequest.wasapproved == True:
            return make_response(jsonify({'message':'Ad Request is already approved'}), 202)
        ad = Ad.query.get(adrequest.ad_id)
        ad.status = 'Open'
        db.session.delete(adrequest)
        db.session.commit()
        return make_response(jsonify({'message':'Ad Request Removed Successfully'}), 200)

# get Ad details

@app.route('/influencer/ad/<int:id>', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer','Admin','Sponsor')
def influencerad(id):
    if request.method == 'GET':
        ad = Ad.query.get(id)
        if not ad:
            return make_response(jsonify({'message':'Ad does not exist'}), 202)
        return make_response(jsonify(ad.formatter()), 200)

# user stats

@app.route('/influencer/stats', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer')
def influencerstats():
    if request.method == 'GET':
        user = User.query.get(current_user.id)
        if not user:
            return make_response(jsonify({'message':'User not found'}), 202)
        adtotal = Adrequest.query.filter_by(user_id=user.id).count()
        adcompleted = Adrequest.query.filter_by(user_id=user.id, status='Completed').count()
        adapproved = Adrequest.query.filter_by(user_id=user.id, wasapproved=True).count()
        adrejected = Adrequest.query.filter_by(user_id=user.id, status='Rejected').count()
        revenue=0
        for transact in Transactions.query.filter_by(user_id=user.id).all():
            if transact.transaction_type == 'Credit':
                revenue += transact.amount

        data = {'total_ad_requests':adtotal,'revenue':revenue ,'rejected':adrejected,'completed_ad_requests':adcompleted, 'totalfollowers':wordtotalreachs(int(user.totalfollowers)), 'approved_ad_requests':adapproved}
        return make_response(jsonify(data), 200)

# Read User Reviews
@app.route('/influencer/reviews', methods=['GET'])
@auth_token_required
@roles_accepted('Influencer')
@cache.cached(timeout=50)
def readreviews():
    if request.method == 'GET':
        if not current_user:
            return make_response(jsonify({'message':'User not found'}), 202)
        reviews = current_user.ratings
        data = []
        for review in reviews:
            data.append(review.formatter())
        return make_response(jsonify({'data':data,'username':current_user.username}), 200)

# Chat with Influencer Route

# get all and send message chats route

@app.route('/influencer/<int:id>/chats', methods=['GET','POST'])
@auth_token_required
@roles_accepted('Influencer')
def allinfluencechats(id):
    if request.method == 'GET':
        adrequest = Adrequest.query.get(id)
        if not adrequest:
            return make_response(jsonify({'message':'Ad Request does not exist'}), 202)
        if adrequest.user_id != current_user.id:
            return make_response(jsonify({'message':'You are not authorized to view this chat'}), 202)
        if adrequest.status == 'Completed':
            return make_response(jsonify({'message':'Ad Request is already completed'}), 202)
        if adrequest.status == 'Rejected':
            return make_response(jsonify({'message':'Ad Request is already rejected'}), 202)
        chats = Messages.query.filter_by(request_id=id).all()
        data = []
        for chat in chats:
            data.append(chat.formatter())
        return make_response(jsonify(data), 200)
    
    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message')
        adreq =Adrequest.query.get(id)
        ad = Ad.query.get(adreq.ad_id)
        campaign = Campaign.query.get(ad.campaign_id)
        receiver = campaign.sponsor_id
        if not message:
            return make_response(jsonify({'message':'Please enter a message'}), 202)
        new_message = Messages(request_id=id, message=message, date_created=datetime.now(), sender=current_user.id, receiver=receiver )
        db.session.add(new_message)
        db.session.commit()
        return make_response(jsonify({'message':'Message Sent Successfully'}), 200)


