from flask import Flask, render_template, request, redirect, url_for

from user import User

app = Flask(__name__)

@app.route("/users")
def users_list_all():
    users = User.get_all()
    return render_template("index.html", users_list = users)

@app.route("/users/new")
def create_new_user():
    return render_template("create.html")

@app.route("/users/add_user", methods=['POST'])
def add_new_user():
    data = {"fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
    new_user_id = User.save(data)
    return redirect(url_for('display_single_user_by_id', user_id = new_user_id))

@app.route("/users/update_user", methods=['POST'])
def update_single_user_by_id():
    print(request.form)
    data = {"user_id": request.form["user_id"],
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
    user_id = User.update_single_user_by_id(data)
    return redirect(url_for('display_single_user_by_id', user_id = user_id))

@app.route("/users/delete_user", methods=['POST'])
def delete_single_user_by_id():
    print(request.form)
    data = {"user_id": request.form["user_id"]
        }
    User.delete_single_user_by_id(data)
    return redirect('/users')

@app.route("/users/<int:user_id>")
def display_single_user_by_id(user_id):
    data = {"user_id": user_id}
    user_data = User.get_single_user_by_id(data)
    return render_template("read.html", user = user_data)

@app.route("/users/<user_id>/edit")
def edit_single_user_by_id(user_id):
    data = {"user_id": user_id}
    user_data = User.get_single_user_by_id(data)
    return render_template("edit.html", user = user_data)

@app.route("/users/<user_id>/destroy")
def destroy_single_user_by_id(user_id):
    data = {"user_id": user_id}
    user_data = User.get_single_user_by_id(data)
    return render_template("delete.html", user = user_data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
