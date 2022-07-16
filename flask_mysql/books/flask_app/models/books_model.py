from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import authors_model
from flask_app import DATABASE

class Books:
    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def list_books(cls):
        query = "SELECT * FROM books ORDER BY title;"
        results = connectToMySQL(DATABASE).query_db(query)
        books_list = []
        for book in results:
            books_list.append( cls(book) )
        return books_list

    @classmethod
    def list_available_authors(cls, data):
        query = "SELECT * "
        query+= "FROM users "
        query+= "WHERE users.id NOT IN "
        query+= "(SELECT user_id FROM favorites WHERE book_id = %(book_id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        authors_list = []
        for author in results:
            authors_list.append(authors_model.Authors(author))
        return authors_list

    @classmethod
    def show_favorites_by_id(cls, data):
        query = "SELECT * "
        query+= "FROM books "
        query+= "LEFT JOIN favorites "
        query+= "ON books.id = favorites.book_id "
        query+= "LEFT JOIN users "
        query+= "ON favorites.user_id = users.id "
        query+= "WHERE books.id = %(id)s "
        query+= "ORDER BY users.last_name;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        book = cls(results[0])
        authors_list = []

        for author in results:
            current_author = {
                "id": author['users.id'],
                "first_name": author['first_name'],
                "last_name": author['last_name'],
                "created_at": author['users.created_at'],
                "updated_at": author['users.updated_at']
            }
            authors_list.append(authors_model.Authors(current_author))
        book.fav_authors = authors_list
        return book
    
    @classmethod
    def add_new(cls, data):
        query = "INSERT INTO books (title, num_of_pages) "
        query+= "VALUES (%(title)s, %(pages)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) "
        query+= "VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)