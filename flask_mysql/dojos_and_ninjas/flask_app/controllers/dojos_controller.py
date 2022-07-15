from flask_app import app
from flask_app.models.dojos_model import Dojo
from flask import render_template, request, redirect

@app.route("/")
@app.route("/dojos")
def dojos_list_all():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos_list = dojos)

@app.route("/dojos/<int:dojo_id>")
def display_dojo_by_id(dojo_id):
    data = {"dojo_id": dojo_id}
    dojo_data = Dojo.get_dojo_with_ninjas(data)
    return render_template("show_dojo.html", dojo_data = dojo_data)

@app.route("/dojos/new_dojo", methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")
