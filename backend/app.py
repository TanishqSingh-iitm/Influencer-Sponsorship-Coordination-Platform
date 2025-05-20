from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from models import user_datastore, db
from datetime import datetime
from flask_security.utils import verify_password, hash_password
from flask_caching import Cache
from Celery.celery_factory import celery_init_app
import flask_excel as excel



def create_app():
    from config import Config
    App = Flask(__name__)
    CORS(App, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes
    App.config.from_object(Config)
    db.init_app(App)
    cache = Cache(App)
    security = Security(App, user_datastore)
    App.cache = cache
    App.app_context().push()
    with App.app_context():
        db.create_all()
        user_datastore.find_or_create_role(name='Admin', description='Administrator of CreativeMerge')
        user_datastore.find_or_create_role(name='Sponsor', description='Sponsors of CreativeMerge')
        user_datastore.find_or_create_role(name='Influencer', description='Influencers of CreativeMerge')
        db.session.commit()
        admin_user = user_datastore.find_user(email='admin@CreativeMerge.com')
        if not admin_user:
            hased_password = hash_password('admin')
            user_admin = user_datastore.create_user(username='Admin', password=hased_password, name='Admin', email='admin@CreativeMerge.com',  bio="Admin of CreativeMerge", date_joined=datetime.now())
            user_datastore.add_role_to_user(user_admin, 'Admin')
        db.session.commit()
    return App



# Initialize the app and security
app = create_app()


# Initialize the celery app

celery_app = celery_init_app(app)


import routes.auth
import routes.admin
import routes.sponsor
import routes.influencer
import Celery.celery_schedule
 
excel.init_excel(app)





'''if __name__ == '__main__':
     app.run(debug=True)'''