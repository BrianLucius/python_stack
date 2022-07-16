from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.another_templates_model import AnotherClassname
from flask_app import DATABASE

class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users ORDER BY last_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        user_list = []
        for user in results:
            user_list.append(cls(user))
        return user_list

    @classmethod
    def all_friendships(cls):
        query = "SELECT * "
        query+= "FROM users "
        query+= "JOIN friendships "
        query+= "ON users.id = friendships.user_id "
        query+= "JOIN users AS friends "
        query+= "ON friendships.friend_id = friends.id "
        query+= "ORDER BY users.last_name;"
        
        results = connectToMySQL(DATABASE).query_db(query)
        user_list = []
        for row in results:
            user_list.append(cls(row))
            # friend_list = []
            # for row
        return user_list 

    @classmethod
    def add_user(cls, data):
        query= "INSERT INTO users (first_name, last_name) "
        query+="VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    
    @classmethod
    def add_friendship(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id) "
        query+= "VALUES (%(user_id)s, %(friend_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)