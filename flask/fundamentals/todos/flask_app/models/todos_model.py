from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Todo:
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query  = "SELECT * "
        query += "FROM todos;"
        result = connectToMySQL(DATABASE).query_db(query)

        list_todos = []
        for todo in result:
            list_todos.append(cls(todo))
        return list_todos

    @classmethod
    def create(cls, data):
        query  = "INSERT INTO todos (description, status, user_id) "
        query += "VALUES (%(description)s, %(status)s, %(user_id)s);"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query+= "FROM todos "
        query+= "WHERE todos.id = %(id)s;"
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        if  len(result) > 0:
            todo = cls(result[0])
        return todo
    
    @classmethod
    def update_one(cls,data):
        query = "UPDATE todos "
        query+= "SET todos.description=%(description)s, todos.status=%(status)s "
        query+= "WHERE todos.id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_todo(cls,data):
        query = "DELETE FROM todos "
        query+= "WHERE todos.id = %(id)s;"
        
        return connectToMySQL(DATABASE).query_db(query, data)

"""
SELECT
get_one()
get_all()

INSERT
create()
save()

UPDATE
update_one()
edit_one()

DELETE
delete_one()
"""