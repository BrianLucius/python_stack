from flask_app import app
from flask_app.models.books_model import Books
from flask_app.models.authors_model import Authors
from flask import render_template, request, redirect

@app.route("/")
@app.route("/books")
def list_books():
    books_list = Books.list_books()
    return render_template("books.html", books_list = books_list)

@app.route("/books/<int:id>")
def show_fav_authors_by_id(id):
    data = {"id": id}
    favorites_list = Books.show_favorites_by_id(data)
    book_id = {"book_id": favorites_list.id}
    authors_list = Books.list_available_authors(book_id)
    return render_template("book_show.html", favorites_list = favorites_list, authors_list = authors_list)

@app.route("/books/add_new", methods=['POST'])
def add_new_book():
    Books.add_new(request.form)
    return redirect("/books")

@app.route("/books/add_favorite", methods=['POST'])
def add_favorite_book():
    Books.add_favorite(request.form)
    return redirect(f"/books/{request.form['book_id']}")
