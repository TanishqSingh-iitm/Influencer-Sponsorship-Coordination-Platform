from flask import render_template, request, redirect, url_for, session, flash, send_file, jsonify, make_response
from flask_security import login_required, current_user
from  app import app
from models import user_datastore, db, Campaign, Ad, Adrequest
from datetime import datetime
from flask_security.utils import verify_password, hash_password
import json
import os



    


# Register Function
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        if data.get('role') == "Sponsor":
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
            
            user = user_datastore.find_user(email=email) or user_datastore.find_user(username=username)
            if user:
                return make_response(jsonify({"message":"User already exists Kindly Choose other username"}),202)
            
            if not user:
                joining =  datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")
                personal_data = {"industry":industry, "site":site, "addinfo":addinfo, "profpic":profpic, "theme":"Null"}
                hashed_password = hash_password(password)
                user = user_datastore.create_user(name=name, username=username,email=email, password=hashed_password, date_joined=joining, active=0, bio=addinfo, personal_data=personal_data)
                if role == "Sponsor":
                    user_datastore.add_role_to_user(user, 'Sponsor')
                db.session.commit()
                return make_response(jsonify({"message":"User registered successfully"}),200)
            
            return make_response(jsonify({"message":" Unknown Error Occured Contact Admin"}),202)

        
        if data.get('role') == "Influencer":
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
            total_followers = 0
            if isyt == True:
                total_followers = total_followers + int(data.get("ytfollowers"))
            if isfb == True:
                total_followers = total_followers + int(data.get("fbfollowers"))
            if isinsta == True:
                total_followers = total_followers + int(data.get("instafollowers"))
            if islinkedin == True:
                total_followers = total_followers + int(data.get("linkedfollowers"))
            if istiktok == True:
                total_followers = total_followers + int(data.get("tikfollowers"))
            if istwitter == True:
                total_followers = total_followers + int(data.get("xfollowers"))
            if issnap == True:
                total_followers = total_followers + int(data.get("snapfollowers"))
            if istwitch == True:
                total_followers = total_followers + int(data.get("twitchfollowers"))
            if iskick == True:
                total_followers = total_followers + int(data.get("kickfollowers"))
            if isthread == True:
                total_followers = total_followers + int(data.get("threadfollowers"))
            

            if is_terms != True:
                return make_response(jsonify({"message":"Please accept the terms and conditions"}), 202)

            if not email or not name or not username or not password or not confirm_password:
                return make_response(jsonify({"message":"Please enter data in all required fields"}), 202)
            
            if confirm_password != password:
                return make_response(jsonify({"message":"Passwords do not match"}),202)
            
            if not isyt and not isfb and not isinsta and not islinkedin and not isthread and not istiktok and not iskick and not istwitch and not istwitter and not issnap:
                return make_response(jsonify({"message":"Please select atleast one social media platform"}),202)

            user = user_datastore.find_user(email=email) or user_datastore.find_user(username=username)

            if user:
                return make_response(jsonify({"message":"User already exists Kindly Choose other username"}),202)

            if not user:
                joining =  datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")
                hashed_password = hash_password(password)
                user = user_datastore.create_user(name=name, username=username,email=email, password=hashed_password, date_joined=joining, bio=addinfo, totalfollowers=total_followers, personal_data=personal_data)
                if role == "Influencer":
                    user_datastore.add_role_to_user(user, 'Influencer')
                db.session.commit()
                return make_response(jsonify({"message":"User registered successfully"}),200)
            return make_response(jsonify({"message":"Unknown Error Occured"}),202)

# Upload Profile Picture Function
@app.route('/uploadprofpic', methods=['POST'])
def uploadprofpic():
    if request.method == 'POST':
        data = request.form
        if data["role"] == "Influencer":
            username = data['username']
            role = data['role']
            image = request.files['file']
            profpic = data['profpic']

            if not image and profpic == True:
                return make_response(jsonify({"message":"Please upload a profile picture"}), 202)
            filename = f"{username}.png"
            storage_path = os.path.join(os.getcwd(), 'Images/InfluencerImg',filename)
            if os.path.isfile(storage_path):
                os.remove(storage_path)
                image.save(storage_path)
            else:
                image.save(storage_path)
            return make_response(jsonify({"message":"Profile Picture Uploaded Successfully"}), 200)
        
        if data["role"] == "Sponsor":
            username = data['username']
            role = data['role']
            image = request.files['file']
            profpic = data['profpic']

            if not image and profpic == True:
                return make_response(jsonify({"message":"Please upload a profile picture"}), 202)
            filename = f"{username}.png"
            storage_path = os.path.join(os.getcwd(), 'Images/SponsorImg',filename)
            if os.path.isfile(storage_path):
                os.remove(storage_path)
                image.save(storage_path)
            else:
                image.save(storage_path)
            return make_response(jsonify({"message":"Profile Picture Uploaded Successfully"}), 200)
        
        return make_response(jsonify({"message":"Unknown Error Occured"}), 202)


# Login Function
@app.route('/signin', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username_email = data.get('text')
        password = data.get('password')
        if not username_email or not password:
            return make_response(jsonify({"message":"Please enter data in all required fields"}), 202)
        
        user = user_datastore.find_user(username=username_email)

        if user:
            if user.active == 0:
                return make_response(jsonify({"message":"Account is not active yet! Please wait until Admin activates your account."}), 202)

            if verify_password(password, user.password):
                user.last_login_at = user.current_login_at 
                user.current_login_at = datetime.now() 
                user.login_count = (user.login_count or 0) + 1
                db.session.commit()
                
                if user.roles[0].name == "Admin":
                    return make_response(jsonify({"message":"Login successful! Welcome Admin", 
                                "authToken": user.get_auth_token(),
                                 "Role": user.roles[0].name,
                                 "id": user.id,
                                 "username":user.username,
                                 }), 200)
                else:
                    return make_response(jsonify({"message":"Login successful", 
                                "authToken": user.get_auth_token(),
                                 "Role": user.roles[0].name,
                                 "id": user.id,
                                 "username":user.username,
                                 "Profilepic":user.personal_data['profpic']}), 200)

            return make_response(jsonify({"message":"Incorrect password"}), 202)
        return make_response(jsonify({"message":"User does not exist"}), 202)
    
