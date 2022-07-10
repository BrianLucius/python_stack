from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    num_items = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['blackberry'])+int(request.form['apple'])
    print(f"Charging {request.form['first_name']} for {num_items} fruits.")
    now = datetime.now()
    date_time = now.strftime("%B %d, %Y %I:%M:%S %p")
    print(f"Order Date: {date_time}")
    return render_template("checkout.html", date_time = date_time, num_items = num_items)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True, port=5001)
