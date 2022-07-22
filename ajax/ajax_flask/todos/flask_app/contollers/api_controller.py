from flask_cors import cross_origin, CORS
from flask_app.models.todos_model import Todo
from flask_app import app
from flask import json, jsonify, request

# cors = CORS(app, resources={r"/api/*": {"origins": ['http://127.0.0.1:5500']}})

@app.route('/api/todos')
@cross_origin(origins=['http://127.0.0.1:5500'])
def api_get_todos():
    list_of_todos = Todo.api_get_all()
    return jsonify(list_of_todos), 200

@app.route('/api/delete/todo/<int:id>', methods = ['DELETE'])
@cross_origin(origins=['http://127.0.0.1:5500'])
def api_delete_one(id):
    data = {
        "id": id
    }
    Todo.delete_todo(data)
    return jsonify({}), 204

@app.route('/api/add/todo', methods=['POST'])
@cross_origin(origins=['http://127.0.0.1:5500'], allow_headers=['Content-type'])
def api_add_one():
    print(request.data.decode('UTF-8'))
    newTodo = json.loads(request.data.decode('UTF-8'))

    todo_id = Todo.create(newTodo)
    data = {
        "id" : todo_id,
        "message" : "Todo added successfully."
    }
    return data, 201
