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
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be more than two characters","error_registration_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be more than two characters","error_registration_last_name")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Your email address is invalid","error_registration_email")
            is_valid = False
        if data['password'] == "":
            flash("You must create a password","error_registration_password")
            is_valid = False
        if data['password_confirmation'] == "":
            flash("Please confirm your password","error_registration_password_confirmation")
            is_valid = False
        if data['password'] != data['password_confirmation']:
            flash("Your passwords do not match","error_registration_password_confirmation")
            is_valid = False
        return is_valid

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
