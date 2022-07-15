from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.another_templates_model import AnotherClassname
from flask_app import DATABASE

class MyClassname:
    def __init__(self , data):
        self.field1 = data['field1']
        self.field2 = data['field2']

    @classmethod
    def class_method(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        var1 = []
        for var_item in results:
            var1.append( cls(var1) )
        return var1