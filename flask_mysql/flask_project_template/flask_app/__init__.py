from flask import Flask
app = Flask(__name__)

app.secret_key = "Supercalifragilisticexpealadocious!"
DATABASE = 'enter_db_name'