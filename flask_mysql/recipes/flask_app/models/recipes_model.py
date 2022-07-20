from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users_model import User
from flask_app import DATABASE

class Recipe:
    def __init__(self , data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.under_30_mins = data['under_30_mins']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query+= "FROM recipes "
        query+= "JOIN users "
        query+= "ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)

        recipes_list = []
        i = 0
        if len(results) > 0:
            for recipe in results:
                recipes_list.append(cls(recipe))
                user_data = {
                    **recipe,
                    "id": recipe['users.id'],
                    "created_at": recipe['users.created_at'],
                    "updated_at": recipe['users.updated_at']
                }
                recipes_list[i].user = User(user_data)
                i+=1
        return recipes_list
    
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * "
        query+= "FROM recipes "
        query+= "JOIN users "
        query+= "ON recipes.user_id = users.id "
        query+= "WHERE recipes.id=%(recipe_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        recipe_listing = []
        recipe_listing=cls(result[0])

        for recipe in result:
            user_data = {
                "id" : recipe['users.id'],
                "first_name" : recipe['first_name'],
                "last_name" : recipe['last_name'],
                "email": recipe['email'],
                "password": recipe['password'],
                "created_at" : recipe['users.created_at'],
                "updated_at" : recipe['users.updated_at']
            }
        recipe_listing.user = User(user_data)
        return recipe_listing

    @classmethod
    def add_one(cls, data):
        query = "INSERT INTO recipes (user_id, name, under_30_mins, description, instructions, date_made) "
        query+= "VALUES (%(user_id)s, %(name)s, %(under_30_mins)s, %(description)s, %(instructions)s, %(date_made)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes "
        query+= "SET name=%(name)s, under_30_mins=%(under_30_mins)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s "
        query+= "WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes "
        query+= "WHERE id=%(recipe_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
