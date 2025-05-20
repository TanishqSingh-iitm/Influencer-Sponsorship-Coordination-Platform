from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_security import UserMixin, RoleMixin, AsaList, SQLAlchemyUserDatastore, Security
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship, backref
import bcrypt
from sqlalchemy.ext.mutable import MutableDict 
from sqlalchemy.types import JSON


db = SQLAlchemy()


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(MutableList.as_mutable(AsaList()), nullable=True)


class User(db.Model, UserMixin):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), unique=True, nullable=False)
        name = db.Column(db.String(64), nullable=False)
        password = db.Column(db.String(128), nullable=False)
        email = db.Column(db.String(128), nullable=True)
        bio = db.Column(db.Text, nullable=True)
        date_joined = db.Column(db.DateTime, nullable=False, default=datetime.now())
        last_login_at = db.Column(db.DateTime())
        current_login_at = db.Column(db.DateTime())
        login_count = db.Column(db.Integer)
        active = db.Column(db.Boolean())
        fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
        confirmed_at = db.Column(db.DateTime())
        personal_data = db.Column(MutableDict.as_mutable(JSON), nullable=True)
        flagged = db.Column(db.Boolean(), default=False)
        reported = db.Column(db.Integer, default=0)
        avgrating = db.Column(db.Float, default=0)
        wallet = db.Column(db.Integer, default=0)
        roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
        totalfollowers = db.Column(db.Integer, default=0)
        
        transactions = db.relationship('Transactions', backref='user', lazy=True, cascade='all, delete-orphan')
        ratings = db.relationship('userratings', backref='user', lazy=True, cascade='all, delete-orphan')
        reports = db.relationship('userreports', backref='user', lazy=True, cascade='all, delete-orphan')
        messages_sent = db.relationship('Messages', foreign_keys='Messages.sender', back_populates='sender_user') 
        messages_received = db.relationship('Messages', foreign_keys='Messages.receiver', back_populates='receiver_user')
        adrequests = db.relationship('Adrequest', back_populates='user', lazy=True, cascade='all, delete-orphan')
        


        def formatteruser(self):
            if self.flagged==1:
                status = 'Flagged'
            else:
                status = 'Unflagged'
            return {
                'id': self.id,
                'username': self.username,
                'name': self.name,
                'email': self.email,
                'status': status,
                'role': self.roles[0].name,
                'reported': self.reported,
                'date_joined': datetime.strftime(self.date_joined, "%Y-%m-%d"),
                'industry': self.personal_data['industry'],
                'active': self.active
            }
        def formatteruserinfluencer(self):
            info = self.personal_data
            totalreach = 0
            for i in info['social_media']:
                if(info['social_media'][i][0]==True):
                    totalreach += int(info['social_media'][i][1]) 
            reach = totalreach
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
            

            if self.flagged==1:
                status = 'Flagged'
            else:
                status = 'Unflagged'

            
            return {
                'id': self.id,
                'username': self.username,
                'name': self.name,
                'email': self.email,
                'status': status,
                'role': self.roles[0].name,
                'reported': self.reported,
                'date_joined': datetime.strftime(self.date_joined, "%Y-%m-%d"),
                'industry': self.personal_data['industry'],
                'active': self.active,
                'niche': self.personal_data['niche'],
                'totalreach': totalreach,
                'yt': self.personal_data['social_media']['youtube'][0],
                'insta': self.personal_data['social_media']['instagram'][0],
                'fb': self.personal_data['social_media']['facebook'][0],
                'twitter': self.personal_data['social_media']['twitter'][0],
                'linkedin': self.personal_data['social_media']['linkedin'][0],
                'tiktok': self.personal_data['social_media']['tiktok'][0],
                'twitch': self.personal_data['social_media']['twitch'][0],
                'snapchat': self.personal_data['social_media']['snapchat'][0],
                'kick': self.personal_data['social_media']['kick'][0],
                'thread': self.personal_data['social_media']['thread'][0],
                'avg_rating': self.avgrating,
                'reach': reach,
                'profile_pic': self.personal_data['profpic']
            }



user_datastore = SQLAlchemyUserDatastore(db, User, Role)

class Campaign(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.Text, nullable=False) 
    description = db.Column(db.Text, nullable=True) 
    start_date = db.Column(db.DateTime, nullable=False) 
    end_date = db.Column(db.DateTime, nullable=False) 
    status = db.Column(db.String(64), nullable=True) 
    budget = db.Column(db.Integer, nullable=False, default=0) 
    target = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.Integer, nullable=False, default=0)
    current = db.Column(db.Integer, nullable=False, default=0) 
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now()) 
    goal = db.Column(db.Text, nullable=True)
    related_industry = db.Column(db.String(256), nullable=False)
    related_niche = db.Column(db.String(256), nullable=False)
    visibility = db.Column(db.String(64), nullable=False, default='private')
    active = db.Column(db.Boolean, nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False) 

    sponsor = db.relationship('User', backref=db.backref('campaigns', lazy=True, cascade='all, delete-orphan'))
    reports = db.relationship('Campaignreports', backref='Campaign', lazy=True, cascade='all, delete-orphan')
    ads = db.relationship('Ad', backref='Campaign', lazy=True, cascade='all, delete-orphan')

    def formatter(self):
        date1 = self.start_date
        date2 = self.end_date
        differencetotal = (date2 - date1).days

        difference = (datetime.now()-date1).days
        duration = (date2 - datetime.now()).days
        if duration<=0:
            duration = 0
        if differencetotal<=0:
            differencetotal = 1
            difference = 1
        campaigncompletion = (difference/differencetotal)*100
        user = User.query.filter_by(id=self.sponsor_id).first()
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_date': datetime.strftime(self.start_date, "%Y-%m-%d"),
            'end_date': datetime.strftime(self.end_date, "%Y-%m-%d"),
            'status': self.status,
            'budget': self.budget,
            'target': self.target,
            'progress': round(self.progress,4),
            'current': self.current,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d"),
            'goal': self.goal,
            'visibility': self.visibility,
            'active': self.active,
            'sponsor': user.name,
            'sponsor_id': self.sponsor_id,
            'related_industry': self.related_industry,
            'related_niche': self.related_niche,
            'campaign_completion': round(campaigncompletion, 2),
            'campaign_duration': duration
        }
    

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(64), nullable=False, default='open')
    baseprice = db.Column(db.Integer, nullable=False)
    negociatedprice = db.Column(db.Integer, nullable=False, default=0)
    isnegociated = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    preferedplatforms = db.Column(db.String(256), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id', ondelete='CASCADE'))
    
    adrequested = db.relationship('Adrequest', back_populates='ad', cascade='all, delete-orphan')
    

    def formatter(self):
        campaign = Campaign.query.filter_by(id=self.campaign_id).first()
        data = {}
        platforms = self.preferedplatforms.split(' ')
        for i in platforms:
            if i=='youtube':
                data['youtube'] = True
            if i=='instagram':
                data['instagram'] = True
            if i=='facebook':
                data['facebook'] = True
            if i=='twitter':
                data['twitter'] = True
            if i=='linkedin':
                data['linkedin'] = True
            if i=='tiktok':
                data['tiktok'] = True
            if i=='twitch':
                data['twitch'] = True
            if i=='snapchat':
                data['snapchat'] = True
            if i=='kick':
                data['kick'] = True
            if i=='thread':
                data['thread'] = True
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'baseprice': self.baseprice,
            'negociatedprice': self.negociatedprice,
            'isnegociated': self.isnegociated,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d"),
            'preferedplatforms': data,
            'campaign': campaign.title,
            'campaign_id': self.campaign_id
        }


class Campaignreports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id', ondelete='CASCADE'))
    issuecategory = db.Column(db.String(256), nullable=False)
    issue = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    submitted_by = db.Column(db.String(256), nullable=False)




    
    def formatter(self):
        campaign = Campaign.query.filter_by(id=self.campaign_id).first()
        return {
            'id': self.id,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
            'campaign': campaign.title,
            'sponsor': campaign.sponsor.name,
            'submitted_by': self.submitted_by,
            'issue': self.issue,
            'description': self.description,
            'issuecategory': self.issuecategory
        }
   

class userreports(db.Model):
    __TableName__ = 'UserReports'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    issue = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    submitted_by = db.Column(db.String(256), nullable=False)
    issuecategory = db.Column(db.String(256), nullable=False)

    def formatter(self):
        return {
            'id': self.id,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
            'issue': self.issue,
            'description': self.description,
            'submitted_by': self.submitted_by,
            'issuecategory': self.issuecategory
        }


class userratings(db.Model):
    __TableName__ = 'UserRatings'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=True)
    submitted_by = db.Column(db.String(256), nullable=False)

    def formatter(self):
        return {
            'id': self.id,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
            'rating': self.rating,
            'review': self.review,
            'submitted_by': self.submitted_by
        }
 


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    def formatter(self):
        return {
            'id': self.id,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'description': self.description
        }

class Adrequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ad_id = db.Column(db.Integer, db.ForeignKey('ad.id'))
    status = db.Column(db.String(256), nullable=False, default='Requested')
    description = db.Column(db.Text, nullable=True)
    negociatedprice = db.Column(db.Integer, nullable=False, default=0)
    granted_at = db.Column(db.DateTime, nullable=True)
    finish_by = db.Column(db.DateTime, nullable=True)
    wasapproved = db.Column(db.Boolean, nullable=False, default=False)
    requested_bysponsor = db.Column(db.Boolean, nullable=False, default=False)
    requested_byinfluencer = db.Column(db.Boolean, nullable=False, default=False)
    
    user = db.relationship('User', back_populates='adrequests')
    ad = db.relationship('Ad', back_populates='adrequested')
    message = db.relationship('Messages', backref='Adrequest', lazy=True, cascade='all, delete-orphan')

    def formatter(self):
        ad = Ad.query.filter_by(id=self.ad_id).first()
        campaign = Campaign.query.filter_by(id=ad.campaign_id).first()
        sponsor = User.query.filter_by(id=campaign.sponsor_id).first()
        user = User.query.filter_by(id=self.user_id).first()
        
        if self.granted_at == None and self.finish_by == None and self.wasapproved == False:
            return {
                'id': self.id,
                'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
                'user_id': self.user_id,
                'ad_id': self.ad_id,
                'status': self.status,
                'description': self.description,
                'negociatedprice': self.negociatedprice,
                'granted_at': self.granted_at,
                'finish_by': self.finish_by,
                'wasapproved': self.wasapproved,
            'ad_title': ad.title,
            'ad_status': ad.status,
            'campaign_title': campaign.title,
            'user_name': user.name,
            'campaignid': campaign.id,
            'sponsor_id': sponsor.id,
            'requested_bysponsor': self.requested_bysponsor,
            'requested_byinfluencer': self.requested_byinfluencer
            }
            
        
        return {
            'id': self.id,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
            'user_id': self.user_id,
            'ad_id': self.ad_id,
            'status': self.status,
            'description': self.description,
            'negociatedprice': self.negociatedprice,
            'granted_at': datetime.strftime(self.granted_at, "%Y-%m-%d %H:%M"),
            'finish_by': datetime.strftime(self.finish_by, "%Y-%m-%d %H:%M"),
            'wasapproved': self.wasapproved,
            'ad_title': ad.title,
            'ad_status': ad.status,
            'campaign_title': campaign.title,
            'user_name': user.name,
            'campaignid': campaign.id,
            'sponsor_id': sponsor.id,
        }



class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    sender = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.Text, nullable=False)
    isread = db.Column(db.Boolean, nullable=True, default=False)
    request_id = db.Column(db.Integer, db.ForeignKey('adrequest.id', ondelete='CASCADE'))


    sender_user = db.relationship('User', foreign_keys=[sender], back_populates='messages_sent') 
    receiver_user = db.relationship('User', foreign_keys=[receiver], back_populates='messages_received')

    def formatter(self):
        send = User.query.filter_by(id=self.sender).first()
        rec = User.query.filter_by(id=self.receiver).first()

        return {
            'id': self.id,
            'date_created': datetime.strftime(self.date_created, "%Y-%m-%d %H:%M"),
            'sender': self.sender,
            'receiver': self.receiver,
            'message': self.message,
            'isread': self.isread,
            'sender_name': send.username,
            'receiver_name': rec.username
        }
   


