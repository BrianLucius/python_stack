from flask_app import app
from flask_app.models.users_model import User
from flask import render_template, request, redirect

@app.route("/")
@app.route("/friendships")
def display_friendships():
    friendships_list = User.all_friendships()
    users_list = User.all_users()
    return render_template("friendships.html", friendships_list = friendships_list, users_list = users_list)

@app.route("/friendships/add_user", methods=['POST'])
def add_user():
    User.add_user(request.form)
    return redirect("/friendships")

@app.route("/friendships/create", methods=['POST'])
def create_friendship():
    User.add_friendship(request.form)
    return redirect("/friendships")
