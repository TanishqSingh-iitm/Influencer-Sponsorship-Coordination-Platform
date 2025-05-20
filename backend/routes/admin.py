from flask import request, jsonify, make_response, render_template
from flask_security import auth_token_required, roles_accepted, current_user, hash_password
from app import app
from models import db, Campaign, User, Transactions, Campaignreports
from datetime import datetime, timedelta
import json
from models import user_datastore, db, Campaign, User, Ad
from Celery.tasks import add
from celery.result import AsyncResult


cache = app.cache

# Admin Routes

# Admin Profile Routes




# Admin Transactions

@app.route('/admin/wallet', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=30)
def admin_transactions():
    if request.method == 'GET':
        transactions = Transactions.query.filter_by(user_id=current_user.id).all()
        data = []
        for transaction in transactions:
            data.append(transaction.formatter())
        response = {'transactions':data, 'balance':current_user.wallet}
        return make_response(jsonify(response), 200)


# Admin Profile
@app.route('/adminprofile', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
def adminprofile():
    if request.method == 'GET':
        user = User.query.get(current_user.id)
        data = {'name':user.name,'id':user.id, 'username':user.username, 'email':user.email, 'role':user.roles[0].name, 'bio':user.bio, 'date_joined':datetime.strftime(user.date_joined, "%Y-%m-%d"), 'last_login':datetime.strftime(user.current_login_at, "%Y-%m-%d %H:%M")}
        return make_response(jsonify(data), 200)

# Edit Admin Profile
@app.route('/adminprofile/edit', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def adminprofile_edit():
    if request.method == 'POST':
        user = User.query.get(current_user.id)
        data = request.get_json()
        newname = data['name']
        newbio = data['bio']
        newpassword = data['password']
        newconfirmpassword = data['confirm_password']
        
        if newpassword != newconfirmpassword:
            return make_response(jsonify({'message':'Passwords do not match'}), 202)
        if newname == '' or newname is None or newpassword == '' or newpassword is None:
                return make_response(jsonify({'message':'Fields cannot be empty'}), 202)
        
        if newbio != '' or newbio is not None:
            user.bio = newbio
        
        user.name = newname
        user.password = hash_password(newpassword)
        db.session.commit()
        return make_response(jsonify({'message':'Profile Updated'}), 200)

# Sponsor Dashboard Routes

# Sponsor Dashboard
@app.route('/admin/sponsordashboard', methods=['GET', 'POST'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=10)
def sponsordashboard():
    if request.method == 'GET':
        users = User.query.filter_by().all()
        data_active = []
        data_inactive = []
        data_flagged = []
        for sponsor in users:
            if sponsor.roles[0].name == 'Sponsor' and sponsor.active == True and sponsor.flagged == False:
                data_active.append(sponsor.formatteruser())
            elif sponsor.roles[0].name == 'Sponsor' and sponsor.active == False and sponsor.flagged == False:
                data_inactive.append(sponsor.formatteruser())
            elif sponsor.roles[0].name == 'Sponsor' and sponsor.flagged == True:
                data_flagged.append(sponsor.formatteruser())
            else:
                continue
        return make_response(jsonify({'active':data_active,'inactive':data_inactive, 'flagged':data_flagged}), 200)

# Flagged Sponsors

# Flag Sponsor
@app.route('/admin/sponsordashboard/<int:uid>/flag', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def flag_sponsor(uid):
    if request.method == 'POST':
        sponsor = user_datastore.find_user(id=uid)
        if not sponsor:
            return make_response(jsonify({'message':'Sponsor does not exist'}), 202)
        if sponsor.flagged == 1:
            return make_response(jsonify({'message':'Sponsor already flagged'}), 202)
        sponsor.flagged = 1
        db.session.commit()
        return make_response(jsonify({'message':'Sponsor has been flagged'}), 200)



# Unflag Sponsor

@app.route('/admin/sponsordashboard/<int:uid>/unflag', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def unflag_sponsor(uid):
    if request.method == 'POST':
        sponsor = user_datastore.find_user(id=uid)
        if not sponsor:
            return make_response(jsonify({'message':'Sponsor does not exist'}), 202)
        if sponsor.flagged == 0:
            return make_response(jsonify({'message':'Sponsor already unflagged'}), 202)
        sponsor.flagged = 0
        db.session.commit()
        return make_response(jsonify({'message':'Sponsor has been unflagged'}), 200)

# Activate Sponsor

@app.route('/admin/sponsordashboard/<int:uid>/activate', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def activate_sponsor(uid):
     user = user_datastore.find_user(id=uid)
     if user and user.has_role('Sponsor'):
         user_datastore.activate_user(user)
         db.session.commit()
         return jsonify({"message":"User activated successfully"})
     return jsonify({"message":"User not found"})

# Deactivate Sponsor

@app.route('/admin/sponsordashboard/<int:uid>/deactivate', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def deactivate_sponsor(uid):
     user = user_datastore.find_user(id=uid)
     if user and user.has_role('Sponsor'):
         user_datastore.deactivate_user(user)
         db.session.commit()
         return jsonify({"message":"User deactivated successfully"})
     return jsonify({"message":"User not found"})



# Influencer Dashboard Routes

# Influencer Dashboard

@app.route('/admin/influencerdashboard', methods=['GET', 'POST'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=10)
def influencerdashboard():
    if request.method == 'GET':
        users = User.query.filter_by().all()
        data_active = []
        data_inactive = []
        data_flagged = []
        for influencer in users:
            if influencer.roles[0].name == 'Influencer' and influencer.active == True and influencer.flagged == False:
                data_active.append(influencer.formatteruserinfluencer())
            elif influencer.roles[0].name == 'Influencer' and influencer.active == False and influencer.flagged == False:
                data_inactive.append(influencer.formatteruserinfluencer())
            elif influencer.roles[0].name == 'Influencer' and influencer.flagged == True:
                data_flagged.append(influencer.formatteruserinfluencer())
            else:
                continue
        return make_response(jsonify({'active':data_active,'inactive':data_inactive, 'flagged':data_flagged}), 200)





# Flag Influencer

@app.route('/admin/influencerdashboard/<int:id>/flag', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def flag_influencer(id):
    if request.method == 'POST':
        influencer = user_datastore.find_user(id=id)
        if not influencer:
            return make_response(jsonify({'message':'Influencer does not exist'}), 202)
        if influencer.flagged == 1:
            return make_response(jsonify({'message':'Influencer already flagged'}), 202)
        influencer.flagged = 1
        db.session.commit()
        return make_response(jsonify({'message':'Influencer has been flagged'}), 200)
    
# Unflag Influencer

@app.route('/admin/influencerdashboard/<int:id>/unflag', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def unflag_influencer(id):
    if request.method == 'POST':
        influencer = user_datastore.find_user(id=id)
        if not influencer:
            return make_response(jsonify({'message':'Influencer does not exist'}), 202)
        if influencer.flagged == 0:
            return make_response(jsonify({'message':'Influencer already unflagged'}), 202)
        influencer.flagged = 0
        db.session.commit()
        return make_response(jsonify({'message':'Influencer has been unflagged'}), 200)

# Activate Influencer

@app.route('/admin/influencerdashboard/<int:id>/activate', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def activate_influencer(id):
     user = user_datastore.find_user(id=id)
     if user and user.has_role('Influencer'):
         user_datastore.activate_user(user)
         db.session.commit()
         return jsonify({"message":"Influcencer's account activated successfully"})
     return jsonify({"message":"User not found"})

# Deactivate Influencer

@app.route('/admin/influencerdashboard/<int:id>/deactivate', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def deactivate_influencer(id):
     user = user_datastore.find_user(id=id)
     if user and user.has_role('Influencer'):
         user_datastore.deactivate_user(user)
         db.session.commit()
         return jsonify({"message":"Influencer's account deactivated successfully"})
     return jsonify({"message":"User not found"})


# Campaign Routes

# Get Campaigns

@app.route('/admin/campaigns', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=10)
def admin_campaigns():
    if request.method == 'GET':
        campaigns = Campaign.query.filter_by().all()
        data = []
        datacompleted = []
        dataflagged = []
        for campaign in campaigns:
            if campaign.status == 'Completed':
                datacompleted.append(campaign.formatter())
            elif campaign.status == 'Flagged':
                dataflagged.append(campaign.formatter())
            else:
                data.append(campaign.formatter())
        return make_response(jsonify({'campaigns':data,'completed':datacompleted, 'flaggedcampaign':dataflagged}), 200)


# Flag Campaign

@app.route('/admin/campaigns/<int:id>/flag', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def flag_campaign(id):
    if request.method == 'POST':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if campaign.status == 'Flagged':
            return make_response(jsonify({'message':'Campaign already flagged'}), 202)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        campaign.status = 'Flagged'
        db.session.commit()
        return make_response(jsonify({'message':'Campaign has been flagged'}), 200)

# Unflag Campaign

@app.route('/admin/campaigns/<int:id>/unflag', methods=['POST'])
@auth_token_required
@roles_accepted('Admin')
def unflag_campaign(id):
    if request.method == 'POST':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign does not exist'}), 202)
        if campaign.status != 'Flagged' :
            return make_response(jsonify({'message':'Campaign already unflagged'}), 202)
        if campaign.status == 'Completed':
            return make_response(jsonify({'message':'Campaign has been completed'}), 202)
        campaign.status = 'Pending'
        db.session.commit()
        return make_response(jsonify({'message':'Campaign has been unflagged'}), 200)






# Admin Statistics

def format_audience(audience): 
    if audience >= 1_000_000_000: 
        return f'{audience // 1_000_000_000} Billion' 
    elif audience >= 1_000_000: 
        return f'{audience // 1_000_000} Million' 
    elif audience >= 1_000: 
        return f'{audience // 1_000} K' 
    else: 
        return str(audience)


# Admin Statistics boxes



@app.route('/admin/statistics', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
def admin_statistics():
    if request.method == 'GET':
        users = User.query.filter_by().all()
        Campaigns = Campaign.query.filter_by().all()
        activeusers = User.query.filter_by(active=True).all()
        inactiveusers = User.query.filter_by(active=False).all()
        flaggedusers = User.query.filter_by(flagged=True).all()
        completedcampaigns = Campaign.query.filter_by(status='Completed').all()
        publiccampaign = Campaign.query.filter_by(visibility='Public').all()
        totalusers = len(users)
        totalinfluencers=0
        totalcampaigns = len(Campaigns)
        totalsponsors = 0
        flaggedsponsors = 0
        flaggedinfluencers = 0
        totalaudience = 0
        for user in users:
            if user.roles[0].name == 'Influencer':
                if user.flagged == True:
                    flaggedinfluencers += 1
                totalaudience += user.totalfollowers
                totalinfluencers += 1
            elif user.roles[0].name == 'Sponsor':
                if user.flagged == True:
                    flaggedsponsors += 1
                totalsponsors += 1
            else:
                continue
        
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
        
        ads = Ad.query.filter_by().all()
        for ad in ads:
            if ad.status == 'Open':
                adopen += 1
            elif ad.status == 'Closed':
                adclosed += 1
            elif ad.status == 'Approved':
                adapproved += 1
            elif ad.status == 'Rejected':
                adrejected += 1
            elif ad.status == 'Pending':
                adpending += 1
            elif ad.status == 'Requested':
                adrequested += 1
            elif ad.status == 'Negociated':
                adnegociated += 1
            elif ad.status == 'Completed':
                adcompleted += 1
            elif ad.status == 'In Progress':
                adinprogress += 1
            else:
                continue
        topinfluencer = User.query.order_by(User.avgrating.desc()).first()
        if topinfluencer and topinfluencer.roles[0].name == 'Influencer':
            topinfluencer = topinfluencer.username
        else:
            topinfluencer = 'No Influencer Yet'
    

        return make_response(jsonify({'total_users':totalusers, 'total_influencers':totalinfluencers,'total_sponsors':totalsponsors,
                                       'revenue':current_user.wallet, 'totalcampaigns':totalcampaigns,'totalactiveusers':len(activeusers)
                                    ,'totalinactiveusers':len(inactiveusers), 'totalflaggedsponsors':flaggedsponsors,'totalflaggedinfluencers':flaggedinfluencers
                                    ,'audience':format_audience(totalaudience),'completedcampaigns':len(completedcampaigns),'publiccampaign':len(publiccampaign),
                                    'adopen':adopen,'adclosed':adclosed,'adapproved':adapproved,'adrejected':adrejected,'adpending':adpending, 'adrequested':adrequested,
                                    'adnegociated':adnegociated,'adcompleted':adcompleted,'adinprogress':adinprogress, 'topinfluencer':topinfluencer, 'totalads':len(ads)}), 200)
                    


# Read Reports Users
@app.route('/admin/<int:id>/reports', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=30)
def read_reports(id):
    if request.method == 'GET':
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({'message':'User not found'}), 202)
        reports = user.reports
        data = []
        for report in reports:
            data.append(report.formatter())
        return make_response(jsonify({'data':data,'username':user.username}), 200) 


# Read Reports Campaigns
@app.route('/admin/campaigns/<int:id>/reports', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=30)
def read_campaign_reports(id):
    if request.method == 'GET':
        campaign = Campaign.query.get(id)
        if not campaign:
            return make_response(jsonify({'message':'Campaign not found'}), 202)
        reports = campaign.reports
        data = []
        for report in reports:
            data.append(report.formatter())
        return make_response(jsonify({'data':data,'campaign':campaign.title}), 200)
    
# Read User Reviews
@app.route('/admin/<int:id>/reviews', methods=['GET'])
@auth_token_required
@roles_accepted('Admin')
@cache.cached(timeout=30)
def read_reviews(id):
    if request.method == 'GET':
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({'message':'User not found'}), 202)
        reviews = user.ratings
        data = []
        for review in reviews:
            data.append(review.formatter())
        return make_response(jsonify({'data':data,'username':user.username}), 200)

    