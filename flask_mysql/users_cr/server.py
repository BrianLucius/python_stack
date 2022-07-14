from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html", users_list = users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/add_user", methods=['POST'])
def add_new_user():
    data = {"fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
