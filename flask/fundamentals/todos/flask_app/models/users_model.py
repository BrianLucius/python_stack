from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.todos_model import Todo
from flask import flash
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_with_todos(cls, data):
        query = "SELECT * "
        query+= "FROM users "
        query+= "LEFT JOIN todos "
        query+= "ON users.id = todos.user_id "
        query+= "WHERE users.id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(results) > 0:
            current_user = cls(results[0])

            list_of_todos = []
            for row in results:
                current_dict = {
                    "id" : row['todos.id'],
                    "status" : row['status'],
                    "description" : row["description"],
                    "created_at" : row['todos.created_at'],
                    "updated_at" : row['todos.updated_at'],
                    "user_id" : row['user_id']
                }
                list_of_todos.append(Todo(current_dict))

            current_user.list_of_todos = list_of_todos
            return current_user
        else:
            return None

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query+= "FROM users "
        query+= "WHERE email=%(email)s AND password = %(password)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
        
    @classmethod
    def get_one_for_registration(cls, data):
        query = "SELECT * "
        query+= "FROM users "
        query+= "WHERE email=%(email)s;"
        print(data)
        results = connectToMySQL(DATABASE).query_db(query, data)

        if len(results) < 1:
            return False
        else:
            return True

    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) "
        query+= "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_login(data):
        is_valid = True
        if len(data['email']) == 0:
            flash("You must provide an email address.", "error_email")
            is_valid = False
        if len(data['password']) == 0:
            flash("You must enter a password.", "error_password")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("Please provide a first name","error_registration_first_name")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Please provide a last name","error_registration_last_name")
            is_valid = False
        if len(data['email']) < 3:
            flash("Please provide an email","error_registration_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("Please provide a password with more than 8 characters","error_registration_password")
            is_valid = False
        if len(data['password_confirm']) < 8:
            flash("Please provide a password with more than 8 characters","error_registration_password_confirm")
            is_valid = False
        if data['password'] != data['password_confirm']:
            flash("Passwords do not match", "error_registration_password_confirm")
            is_valid = False
        return is_valid
