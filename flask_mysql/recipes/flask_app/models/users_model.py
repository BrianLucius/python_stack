import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app, DATABASE
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_UPPER_COMPLEXITY_REGEX = re.compile(r'^(?:.*[A-Z])')
PW_NUMBER_COMPLEXITY_REGEX = re.compile(r'^(?:.*\d)')

class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def add_new(cls,data):
        data = {
            **data,
            "password": bcrypt.generate_password_hash(data['password'])
        }
        query = "INSERT INTO users (first_name, last_name, email, password) "
        query+= "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def authenticate(cls, data):
        user_in_db = User.get_by_email(data)
        if not user_in_db:
            flash("Invalid Email or Password","error_login_invalid_credentials")
            return False
        if not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Invalid Email or Password","error_login_invalid_credentials")
            return False
        return user_in_db

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users "
        query+= "WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        return None

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users "
        query+= "WHERE id = %(id)s;"
        print(data)
        data = {
            "id": data
        }
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        return None

    @staticmethod
    def validate_registration(data):
        valid_registration = True
        if len(data['first_name']) < 2:
            flash("First name must be more than two characters.", "registration_error_first_name")
            valid_registration = False
        if len(data['last_name']) < 2:
            flash("Last name must be more than two characters.", "registration_error_last_name")
            valid_registration = False
        if len(data['email']) < 3:
            flash("Email must be more than three characters.", "registration_error_email")
            valid_registration = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Email address is not valid.", "registration_error_email")
            valid_registration = False
        elif User.get_by_email(data):
            flash("Email address already in use. Select another address.", "registration_error_email")
            valid_registration = False
        if len(data['password']) < 8:
            flash("Password must be more than eight characters.", "registration_error_password")
            valid_registration = False
        elif not (PW_UPPER_COMPLEXITY_REGEX.match(data['password']) and PW_NUMBER_COMPLEXITY_REGEX.match(data['password'])):
            flash("Password must have at least one number and one uppercase character.", "registration_error_password")
            valid_registration = False
        if data['password'] != data['confirm_password'] or data['confirm_password'] == "":
            flash("Passwords do not match.", "registration_error_confirm_password")
            valid_registration = False
        return valid_registration

    @staticmethod
    def validate_login(data):
        valid_login = True
        if len(data['email']) == 0:
            flash("You must provide a valid email address.", "login_error_email")
            valid_login = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Email address is not valid.", "login_error_email")
            valid_login = False
        if len(data['password']) == 0:
            flash("You must provide a password.", "login_error_password")
            valid_login = False
        return valid_login
