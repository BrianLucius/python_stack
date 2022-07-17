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
        i = 0
        
        for row in results:
            user_list.append(cls(row))
            friend_data = {
                "id" : row['friends.id'],
                "first_name" : row['friends.first_name'],
                "last_name" : row['friends.last_name'],
                "created_at" : row['friends.created_at'],
                "updated_at" : row['friends.updated_at']
            }
            user_list[i].friend = cls(friend_data)
            i+=1
        return user_list
    
    @classmethod
    def is_friendship(cls, data):
        query= "SELECT 1 AS is_friendship FROM friendships "
        query+="WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return len(results)>0

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