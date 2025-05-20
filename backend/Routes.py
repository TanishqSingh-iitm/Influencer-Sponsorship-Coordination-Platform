from flask import render_template, request, redirect, url_for, session, flash, send_file, jsonify, make_response
from app import app
from models import User, db, user_datastore
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
from datetime import datetime, timedelta
import csv



# Login Function

@app.route('/signin', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username_email = data.get('text')
        password = data.get('password')
        if not username_email or not password:
            return make_response(jsonify({"message":"Please enter data in all required fields"}), 202)
        
        user = user_datastore.find_user(username=username_email) or user_datastore.find_user(email=username_email)
        if user:
            if verify_password(password, user.password):
                return make_response(jsonify({"message":"Login successful", 
                                "authToken": user.get_auth_token(),
                                 "Role": user.roles[0].name,
                                 "id": user.id,}), 200)
            return make_response(jsonify({"message":"Incorrect password"}), 202)
        return make_response(jsonify({"message":"User does not exist"}), 202)