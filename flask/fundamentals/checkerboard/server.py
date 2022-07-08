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

@app.route('/', defaults={'x': int(2), 'y': int(2), 'boxColor1': 'black', 'boxColor2': 'red'})
@app.route('/<int:x>', defaults={'y': int(2), 'boxColor1': 'black', 'boxColor2': 'red'})
@app.route('/<int:x>/<int:y>', defaults={'boxColor1': 'black', 'boxColor2': 'red'})
@app.route('/<int:x>/<int:y>/<boxColor1>', defaults={'boxColor2': 'red'})
@app.route('/<int:x>/<int:y>/<boxColor1>/<boxColor2>')
def checkerboard(x, y, boxColor1, boxColor2):
    return render_template('index.html', xSize=x, ySize=y, boxColor1=boxColor1, boxColor2 = boxColor2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.