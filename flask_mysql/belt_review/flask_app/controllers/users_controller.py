from flask_app import app
from flask_app.models.user_model import User
from flask import render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def display_login():
    return render_template("login.html")

@app.route("/user/registration", methods=['POST'])
def process_registration():
    # validate the registration form
    if not User.validate_registration(request.form):
        return redirect('/')
    # Connect to the model
    # Validate if the user already exists
    user_exists = User.get_one_to_validate_email(request.form)
    if user_exists is not None:
        flash("This email already exists","error_registration_email")
        return redirect('/')
    # Proceed to create the user
    data = {
        **request.form,
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.create(data)

    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect("/recipes")

@app.route("/user/login", methods=['POST'])
def process_login():
    if not User.validate_login(request.form):
        return redirect('/')
    current_user = User.get_one_to_validate_email(request.form)
    if current_user is not None:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Error logging in, please try again", "error_login_invalid_credentials")
            return redirect("/")

        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['user_id'] = current_user.id

        return redirect('/recipes')
    flash("Error logging in, please try again", "error_login_invalid_credentials")
    return redirect('/')

@app.route("/user/logout")
def process_logout():
    session.clear()
    return redirect('/')
