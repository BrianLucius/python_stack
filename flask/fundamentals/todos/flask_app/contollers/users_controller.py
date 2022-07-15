from flask_app import app
from flask_app.models.users_model import User
from flask import render_template, redirect, request, session
from flask_app import list_of_users

@app.route('/user/<int:id>/todos')
def get_user_by_id_with_todos(id):
    data = {
        "id": id
    }
    current_user = User.get_one_with_todos(data)
    return render_template("user_todos.html", current_user = current_user)

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
    session['logged_in_user'] = request.form['user_id']
    return redirect('/todos')