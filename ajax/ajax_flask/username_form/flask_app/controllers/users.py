from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/users/create', methods=['POST'])
def create_user():
    result = User.save(request.form)
    data = {
        "message" : "Added a user!",
        "id" : result
    }
    return jsonify(data), 201
