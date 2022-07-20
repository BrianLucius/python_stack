from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app import DATABASE
from flask import flash

class Recipe:
    def __init__(self , data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooked_date = data['cooked_date']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * "
        query += "FROM recipes "
        query += "JOIN users "
        query += "ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)

        list_recipes = []

        for row in results:
            current_recipe = cls(row)
            user_data = {
                **row,
                "id": row['users.id'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            current_user = User(user_data)
            current_recipe.user = current_user
            list_recipes.append(current_recipe)
        return list_recipes

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * "
        query+= "FROM recipes "
        query+= "JOIN users "
        query+= "ON recipes.user_id = users.id "
        query+= "WHERE recipes.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if len(result) > 0:
            current_recipe = cls(result[0])
            user_data = {
                **result[0],
                "id": result[0]['users.id'],
                "created_at": result[0]['users.created_at'],
                "updated_at": result[0]['users.updated_at']
            }
            current_recipe.user = User(user_data)
            return current_recipe
        return None

    @classmethod
    def update_one(cls,data):
        query = "UPDATE recipes "
        query+= "SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, cooked_date=%(cooked_date)s "
        query+= "WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, cooked_date, under_30)"
        query+= "VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(cooked_date)s, %(under_30)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) == "":
            flash("Recipe name is required","error_recipe_name")
            is_valid = False
        if len(data['name']) < 3:
            flash("Recipe must be at least three characters","error_recipe_name")
            is_valid = False
        if len(data['description']) == "":
            flash("Description is required","error_recipe_description")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be more than three characters","error_recipe_description")
            is_valid = False
        if len(data['instructions']) == "":
            flash("Instructions are required","error_recipe_instructions")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be more than three characters","error_recipe_instructions")
            is_valid = False
        if data['cooked_date'] == "":
            flash("Cooked date is required","error_recipe_cooked_date")
            is_valid = False
        if not 'under_30' in data:
            flash("Select a value for Under 30 Minutes","error_recipe_under_30")
            is_valid = False
        return is_valid
    