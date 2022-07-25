from flask_app import app
from flask_app.models.user_model import User
from flask import render_template, request, redirect, flash, session, jsonify
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def display_login():
    return render_template("login.html")

@app.route("/user/registration", methods=['POST'])
def process_registration():
    # Validate form data
    result = User.validate_registration(request.form)
    if not result['is_valid']:
        response = {
            'message' : result['messages']
        }
        return jsonify(response), 200
    # Determine if email is already registered
    user_exists = User.get_one_to_validate_email(request.form)
    if user_exists is not None:
        response = {
            'message' : {'error_registration_email' : "This email already exists"}
        }
        return jsonify(response), 200
    # If all is good, register user in DB
    data = {
        **request.form,
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.create(data)
    # //TODO: add query execution validation in case DB is down/unavailable/fails
    # Set session vars and return success message
    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id
    response = {
        "message" : "success"
    }
    return jsonify(response), 201

@app.route("/user/login", methods=['POST'])
def process_login():
    result =  User.validate_login(request.form)
    if not result['is_valid']:
        response = {
            'message' : result['messages']
        }
        return jsonify(response), 200

    current_user = User.get_one_to_validate_email(request.form)

    if current_user:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            response = {
                'message' : {'login_error_invalid_credentials' : "Error logging in, please try again"}
            }
            return jsonify(response), 200

        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['user_id'] = current_user.id

        response = {
        "message" : "success"
        }
        return jsonify(response), 200
    
    response = {
                'message' : {'login_error_invalid_credentials' : "Error logging in, please try again"}
            }
    return jsonify(response), 200

@app.route("/user/logout")
def process_logout():
    session.clear()
    return redirect('/')
