from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello Python July 2022 class!<h1>"

@app.route('/python/<name>/<age>')
def python(name, age):
    print(f"Recieved <{name}> from browser") # for debugging
    return f"<h2>I am a python named {name} who is {age}<h2>"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.
