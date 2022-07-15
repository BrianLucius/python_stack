from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.todos_model import Todo
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
        query+= "JOIN todos "
        query+= "ON users.id = todos.user_id "
        query+= "WHERE users.id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
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
