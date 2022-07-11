from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Supercalifragilisticexpialidocious!"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_survey_form():
    session.clear()
    print("Form submission: ", request.form)
    print("Newsletter Subscriptions list: ", request.form.getlist('newsletter_subscriptions'))
    for key in request.form:
        session[key] = request.form[key]
    return redirect('/result')

@app.route('/result')
def show_survey_form():
    return render_template('/results.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
