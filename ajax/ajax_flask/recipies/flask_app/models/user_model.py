from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.another_templates_model import AnotherClassname
from flask_app import DATABASE
from flask import flash
from flask_app import EMAIL_REGEX

class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_to_validate_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if len(result) > 0:
            current_user = cls(result[0])
            return current_user
        return None

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password)"
        query+= "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @staticmethod
    def validate_registration(data):
        response_message = {}
        response_message["is_valid"] = True
        messages={}
        if len(data['first_name']) < 2:
            messages["error_registration_first_name"] = "First name must be more than two characters"
            response_message["is_valid"] = False
        if len(data['last_name']) < 2:
            messages["error_registration_last_name"] = "Last name must be more than two characters"
            response_message["is_valid"] = False
        if not EMAIL_REGEX.match(data['email']):
            messages["error_registration_email"] = "Your email address is invalid"
            response_message["is_valid"] = False
        if data['password'] == "":
            messages["error_registration_password"] = "You must create a password"
            response_message["is_valid"] = False
        if data['password_confirmation'] == "":
            messages["error_registration_password_confirmation"] = "Please confirm your password"
            response_message["is_valid"] = False
        if data['password'] != data['password_confirmation']:
            messages["error_registration_password_confirmation"] = "Your passwords do not match"
            response_message["is_valid"] = False
        if messages:
            response_message['messages'] = messages
        return response_message

    @staticmethod
    def validate_login(data):
        response_message = {}
        response_message["is_valid"] = True
        messages={}
        if len(data['email']) == 0:
            messages["login_error_email"] = "You must provide a valid email address."
            response_message["is_valid"] = False
        elif not EMAIL_REGEX.match(data['email']):
            messages["login_error_email"] = "Email address is not valid."
            response_message["is_valid"] = False
        if len(data['password']) == 0:
            messages["login_error_password"] = "You must provide a password."
            response_message["is_valid"] = False
        if messages:
            response_message['messages'] = messages
        return response_message
