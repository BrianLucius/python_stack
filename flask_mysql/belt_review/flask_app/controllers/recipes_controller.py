from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask import render_template, request, redirect, flash, session

#move to recipes controller
@app.route("/recipes")
def display_recipes():
    if 'email' not in session:
        return redirect('/')
    #grab all recipes
    recipe_list = Recipe.get_all_with_users()
    return render_template('recipes.html', recipe_list = recipe_list)

@app.route('/recipes/new')
def display_create_recipe():
    if 'email' not in session:
        return redirect('/')
    return render_template('create_recipe.html')

@app.route('/recipes/<int:id>')
def get_one(id):
    if 'email' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    current_recipe = Recipe.get_one_with_user(data)
    return render_template('recipe.html', current_recipe = current_recipe)

@app.route('/recipes/<int:id>/edit')
def display_update_recipe(id):
    if 'email' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    current_recipe = Recipe.get_one_with_user(data)
    return render_template("update_recipe.html", current_recipe = current_recipe)

@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if 'email' not in session:
        return redirect('/')
    # add validation for session and data
    if Recipe.validate_recipe(request.form) is False:
        return redirect(f'/recipes/{id}/update')
    recipe_data = {
        **request.form,
        "id": id
    }
    Recipe.update_one(recipe_data)
    return redirect("/recipes")

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if 'email' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    Recipe.delete_one(data)
    return redirect('/recipes')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'email' not in session:
        return redirect('/')
    #validate
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    #create the recipe
    #redirect to /recipes

    data = {
        **request.form,
        "user_id": session['user_id']
    }

    Recipe.create(data)
    return redirect('/recipes')
