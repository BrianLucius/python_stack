from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    # print(friends)
    return render_template("index.html", friends = friends)

@app.route("/create_friend", methods=['POST'])
def add_friend():
    data = {"fname": request.form["fname"],
            "lname": request.form["lname"],
            "occ": request.form["occ"]
        }
    print("Method returned value: ",Friend.save(data))
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
