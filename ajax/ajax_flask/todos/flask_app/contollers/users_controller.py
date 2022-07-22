from flask_app import app
from flask_app.models.users_model import User
from flask import render_template, redirect, request, session, flash
from flask_app import list_of_users

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/user/<int:id>/todos')
def get_user_by_id_with_todos(id):
    data = {
        "id": id
    }
    current_user = User.get_one_with_todos(data)
    return render_template("user_todos.html", current_user = current_user)

@app.route('/')
@app.route('/user/login')
def user_login():
    return render_template("user_login.html", users = list_of_users)

@app.route('/user/logout')
def user_logout():
    # deleted_id = session.pop('logged_in_user') # will return a value
    # session.clear() # will clear everything in session
    del session['logged_in_user'] # works like pop but does not return a value
    return redirect('/user/login')

@app.route('/user/process_login', methods=['POST'])
def process_login():
    is_valid = User.validate_login(request.form)
    if is_valid == False:
        return redirect('/user/login')

    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    current_user = User.get_one(data)
    if current_user is not False:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Invalid Credentials (pass)","error_login_invalid_credentials")
            return redirect("/user/login")
        session['logged_in_user'] = int(current_user.id)
        return redirect('/todos')
    else:
        flash("Invalid user credentials (general)","error_login_invalid_credentials")
        return redirect('/user/login')

@app.route('/user/process_registration', methods=['POST'])
def process_registration():
    is_valid = User.validate_registration(request.form)
    if is_valid is False:
        return redirect('/user/login')

    data = {
        "email": request.form['email']
    }
    result = User.get_one_for_registration(data)
    if result is not False:
        flash("That email is already in use. Please choose another email.", "error_registration_email")
        return redirect('/user/login')

    user_data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = int(User.create_one(user_data))
    if user_id is not False:
        session['logged_in_user'] = user_id
        return redirect('/todos')
    flash("Something went wrong with the query!", "error_registration_query")
    return redirect('/user/login')
