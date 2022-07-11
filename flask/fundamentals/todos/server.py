from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

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
    return render_template('todos.html', todos = list_of_todos)

@app.route('/todo/form')
def display_todo_form():
    return render_template( 'todo_form.html', users = list_of_users)

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
    list_of_todos.append(request.form)
    return redirect('/todos')


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
