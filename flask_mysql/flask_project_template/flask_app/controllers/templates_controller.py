from flask_app import app
from flask_app.models.template_model import MyClassname
from flask import render_template, request, redirect

@app.route("/")
@app.route("/default")
def controller_action():
    var = MyClassname.class_method()
    return render_template("template.html", varToPass = var)

@app.route("/default/<int:var1>")
def controller_action_with_data(var1):
    data = {"var1": var1}
    returned_data = MyClassname.class_method(data)
    return render_template("template.html", varToPass = returned_data)

@app.route("/default/new_data", methods=['POST'])
def controller_action_create_from_form():
    MyClassname.class_method(request.form)
    return redirect("/default")
