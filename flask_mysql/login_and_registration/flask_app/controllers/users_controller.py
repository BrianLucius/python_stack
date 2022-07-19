from flask_app import app
from flask_app.models.users_model import User
from flask import render_template, request, redirect, session, flash

@app.route("/")
def user_auth():
    return render_template("index.html")

@app.route("/dashboard")
def display_dashboard():
    if session:
        return render_template("dashboard.html", user = User.get_one(session['logged_in_id']))
    return redirect("/")

@app.route("/register", methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect("/")
    session['logged_in_id'] = User.add_new(request.form)
    return redirect("/dashboard")

@app.route("/login", methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect("/")
    authentication = User.authenticate(request.form)
    if not authentication:
        return redirect("/")
    session['logged_in_id'] = authentication.id
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
