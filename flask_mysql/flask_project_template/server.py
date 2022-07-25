from flask_app import app
from flask_app.controllers import templates_controller
from flask_app.controllers import yyy_controller

if __name__ == "__main__":
    app.run(debug=True, port=5001)
