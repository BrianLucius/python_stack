from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo
from flask import render_template, request, redirect

@app.route("/ninjas")
def add_new_ninja():
    dojos=Dojo.get_all()
    return render_template("new_ninja.html", dojos_list = dojos)

@app.route("/ninjas/new_ninja", methods=['POST'])
def create_ninja():
    dojo_id = Ninja.create_ninja(request.form)
    return redirect(f"/dojos/{dojo_id}")
