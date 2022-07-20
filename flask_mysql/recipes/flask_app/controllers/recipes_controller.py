from flask_app import app
from flask_app.models.users_model import User
from flask_app.models.recipes_model import Recipe
from flask import render_template, request, redirect, session

@app.route("/recipes")
def recipes():
    if session:
        return render_template("recipes.html", user = User.get_one(session['logged_in_id']), recipe_list = Recipe.get_all())
    return redirect("/")

@app.route("/recipes/new")
def new_recipe():
    return render_template("new_recipe.html")

@app.route("/recipes/<int:recipe_id>")
def display_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    recipe = Recipe.get_one_by_id(data)
    return render_template("display_recipe.html", recipe = recipe, user = User.get_one(session['logged_in_id']))

@app.route("/recipes/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    recipe = Recipe.get_one_by_id(data)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route("/recipes/add_new", methods=['POST'])
def add_one():
    data = {
        **request.form,
        "user_id": session['logged_in_id']
    }
    Recipe.add_one(data)
    return redirect("/recipes")

@app.route("/recipes/edit_recipe", methods=['POST'])
def update_one():
    Recipe.update_one(request.form)
    return redirect("/recipes")
    
@app.route("/recipes/delete/<int:recipe_id>")
def delete_one(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    Recipe.delete_one(data)
    return redirect("/recipes")


