from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhh"

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

DATABASE = "todos_db"