from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/play/')
# def indexDefault():
#     return render_template('index.html', numBoxes = 3)

# @app.route('/play/<int:numBoxes>')
# def indexNumBoxes(numBoxes):
#     return render_template('index.html', numBoxes = numBoxes)

# @app.route('/play/<int:numBoxes>/<string:boxColor>')
# def indexNumBoxesColor(numBoxes, boxColor):
#     return render_template('index.html', numBoxes = numBoxes, boxColor = boxColor)

@app.route('/play/', defaults={'numBoxes': int(3), 'boxColor': 'cornflowerblue'})
@app.route('/play/<int:numBoxes>', defaults={'boxColor': 'cornflowerblue'})
@app.route('/play/<int:numBoxes>/<string:boxColor>')
def indexNumBoxesColor(numBoxes, boxColor):
    return render_template('index.html', numBoxes = numBoxes, boxColor = boxColor)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.