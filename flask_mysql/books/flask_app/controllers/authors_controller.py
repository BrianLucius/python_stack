from flask_app import app
from flask_app.models.authors_model import Authors
from flask_app.models.books_model import Books
from flask import render_template, request, redirect

@app.route("/")
@app.route("/authors")
def list_authors():
    authors_list = Authors.list_authors()
    return render_template("authors.html", authors_list = authors_list)

@app.route("/authors/<int:id>")
def show_fav_books_by_id(id):
    data = {"id": id}
    favorites_list = Authors.show_favorites_by_id(data)
    author_id = {"user_id": favorites_list.id}
    books_list = Authors.list_available_books(author_id)
    return render_template("author_show.html", favorites_list=favorites_list, books_list=books_list)

@app.route("/authors/add_new", methods=['POST'])
def add_new_author():
    Authors.add_new(request.form)
    return redirect("/authors")

@app.route("/authors/add_favorite", methods=['POST'])
def add_favorite_author():
    Authors.add_favorite(request.form)
    return redirect(f"/authors/{request.form['user_id']}")
