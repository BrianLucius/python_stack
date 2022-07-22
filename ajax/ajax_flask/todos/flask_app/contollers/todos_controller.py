from flask_app import app
from flask_app.models.todos_model import Todo
from flask_app.models.users_model import User
from flask import render_template, redirect, request, session
from flask_app import list_of_users

@app.route('/')
@app.route('/todos')
def get_todos():
    if "logged_in_user" not in session:
        return redirect('/user/login')
    logged_uid = {"id": int(session['logged_in_user'])}
    list_of_todos = Todo.get_all()

    data = {
        "id": session['logged_in_user']
    }
    user = User.get_one_with_todos(data)
    return render_template('todos.html', todos = list_of_todos, user = user)

@app.route('/todo/form')
def display_todo_form():
    if "logged_in_user" not in session:
        return redirect('/user/login')

    data = {
        "id" : session['logged_in_user']
    }
    return render_template( 'todo_form.html', users = list_of_users, user = User.get_one_with_todos(data))

@app.route('/todo/new', methods=['POST'])
def create_todo():
    if session['logged_in_user'] != int(request.form['user_id']):
        return "Hey that's not you"
    new_todo = {"description" : request.form['description'],
                "status" : request.form['status'],
                "user_id" : int(request.form['user_id'])
                }
    Todo.create(new_todo)
    return redirect('/todos')

@app.route('/todo/<int:id>/form')
def display_todo_update_form(id):
    # Create a method to grab the current todo
    data = {
        "id" : id
    }
    current_todo = Todo.get_one(data)
    return render_template('update_todo_form.html', current_todo = current_todo)

@app.route('/todo/<int:id>/update', methods=['POST'])
def update_todo(id):
    data = {
        "id": id,
        "description": request.form['description'],
        "status": request.form['status']
    }
    Todo.update_one(data)
    return redirect(f"/user/{session['logged_in_user']}/todos")

@app.route('/todo/<int:id>/delete', methods=['GET'])
def delete_todo(id):
    data = {
        "id": id
    }
    Todo.delete_todo(data)
    return redirect(f"/user/{session['logged_in_user']}/todos")

"""
Method: GET
#sending everything, use plural
URL: '/users'
Function: get_users()
URL: '/todos' 
Function: get_todos(), get_all_todos()

Method: GET
#One of a particular type
URL: '/todo/<int:id>'
Function: get_todo_by_id()
URL: '/user/<int:id>'
Function: get_user_by_id()

Method: GET
#Displaying a form for a type
URL: '/todo/form'
Function: display_todo_form()

Method: POST
#Creating a new type
URL: '/todo/new'
Function: create_todo()

Method: POST
#Update todo form
URL: '/todo/update/form/<int:id>'
Function: 
"""