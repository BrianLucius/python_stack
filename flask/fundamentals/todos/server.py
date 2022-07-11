from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "This is a secret key"

list_of_users = [
    {"first_name" : "Alex",
     "last_name" : "Miller",
     "id" : 1},
    {"first_name" : "Martha",
     "last_name" : "Smith",
     "id" : 2},
    {"first_name" : "Roger",
     "last_name" : "Anderson",
     "id" : 3}
]

list_of_todos = [
    {"description" : "Learn Python",
     "status" : "complete",
     "id" : "1",
     "user_id" : "1"
    },
    {"description" : "Learn OOP",
     "status" : "complete",
     "id" : "2",
     "user_id" : "1"
    },
    {"description" : "Learn routes in Flask",
     "status" : "in_progress",
     "id" : "3",
     "user_id" : "2"
    },
    {"description" : "Learn POST",
     "status" : "in_progress",
     "id" : "4",
     "user_id" : "3"
    }
]

@app.route('/todos')
def get_todos():
    if "logged_in_user" not in session:
        return redirect('/user/login')
    logged_uid = int(session['logged_in_user'])
    user_acct = list_of_users[logged_uid-1]
    return render_template('todos.html', todos = list_of_todos, user = user_acct)

@app.route('/todo/form')
def display_todo_form():
    if "logged_in_user" not in session:
        return redirect('/user/login')
    logged_uid = int(session['logged_in_user'])
    user_acct = list_of_users[logged_uid-1]
    next_todo_id = len(list_of_todos) + 1
    return render_template( 'todo_form.html', users = list_of_users, user = user_acct, todo_id = next_todo_id)

@app.route('/todo/new', methods=['POST'])
def create_todo():
    print(request.form)
    # new_todo = {
    #     "id" : int(request.form['id']),
    #     "description" : request.form['description'],
    #     "status" : request.form['status'],
    #     "user_id" : int(request.form['user_id'])
    # }
    # list_of_todos.append(new_todo)
    if session['logged_in_user'] != request.form['user_id']:
        return "Hey that's not you"
    else: list_of_todos.append(request.form)
    return redirect('/todos')

@app.route('/user/login')
def user_login():
    return render_template("user_login.html", users = list_of_users)

@app.route('/user/process_login', methods=['POST'])
def process_login():
    session['logged_in_user'] = request.form['user_id']
    return redirect('/todos')

@app.route('/user/logout')
def user_logout():
    # deleted_id = session.pop('logged_in_user') # will return a value
    # session.clear() # will clear everything in session
    del session['logged_in_user'] # works like pop but does not return a value
    return redirect('/user/login')

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
Fucntion: create_todo()
"""

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.
