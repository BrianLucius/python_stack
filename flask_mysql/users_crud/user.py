from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []

        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_single_user_by_id(cls, data):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id=%(user_id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_single_user_by_id(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id=%(user_id)s;"
        connectToMySQL('users_schema').query_db(query, data)
        return

    @classmethod
    def delete_single_user_by_id(cls, data):
        query = "DELETE FROM users WHERE id=%(user_id)s;"
        connectToMySQL('users_schema').query_db(query, data)
        return

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        return connectToMySQL('users_schema').query_db(query, data)
