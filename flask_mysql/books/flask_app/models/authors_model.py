from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books_model
from flask_app import DATABASE

class Authors:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def list_authors(cls):
        query = "SELECT * FROM users ORDER by last_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors_list = []
        for author in results:
            authors_list.append(cls(author))
        return authors_list
    
    @classmethod
    def list_available_books(cls, data):
        query = "SELECT * "
        query+= "FROM books "
        query+= "WHERE books.id NOT IN "
        query+= "(SELECT book_id FROM favorites WHERE user_id = %(user_id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        books_list = []
        for book in results:
            books_list.append(books_model.Books(book))
        return books_list

    @classmethod
    def show_favorites_by_id(cls, data):
        query = "SELECT * "
        query+= "FROM users "
        query+= "LEFT JOIN favorites "
        query+= "ON users.id = favorites.user_id "
        query+= "LEFT JOIN books "
        query+= "ON favorites.book_id = books.id "
        query+= "WHERE users.id = %(id)s "
        query+= "ORDER BY books.title;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        author = cls(results[0])
        books_list = []

        for book in results:
            current_book = {
                "id": book['books.id'],
                "title": book['title'],
                "num_of_pages": book['num_of_pages'],
                "created_at": book['books.created_at'],
                "updated_at": book['books.updated_at']
            }
            books_list.append(books_model.Books(current_book))
        author.fav_books = books_list
        return author
    
    @classmethod
    def add_new(cls, data):
        query = "INSERT INTO users (first_name, last_name) "
        query+= "VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) "
        query+= "VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
