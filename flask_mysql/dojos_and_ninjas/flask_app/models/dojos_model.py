from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_model

class Dojo:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT id, name, created_at, updated_at FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * "
        query+= "FROM dojos LEFT JOIN ninjas "
        query+= "ON dojos.id = ninjas.dojo_id "
        query+= "WHERE dojos.id=%(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])

        for ninja in results:
            ninja_data = {
                "id": ninja["ninjas.id"],
                "dojo_id": ninja["dojo_id"],
                "first_name": ninja["first_name"],
                "last_name": ninja["last_name"],
                "age": ninja["age"],
                "created_at": ninja["ninjas.created_at"],
                "updated_at": ninja["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninjas_model.Ninja(ninja_data))
        return dojo

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) "
        query+= "VALUES (%(name)s);"
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return