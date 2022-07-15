from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, name, created_at, updated_at FROM dojos;"
        results = connectToMySQL('DATABASE').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) "
        query+= "VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        connectToMySQL(DATABASE).query_db(query, data)
        return data['dojo_id']
