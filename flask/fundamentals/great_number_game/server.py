from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Supercalifragilisticexpialidocious!"

@app.route('/')
def main():
    if 'random_num' not in session:
        print("Generating and storing random number...")
        session['random_num'] = random.randint(1, 100)
        print(session['random_num'])
    if 'num_guesses' not in session:
        session['num_guesses'] = 0
    return render_template('index.html', hint="", random_num="")

@app.route('/guess', methods=['POST'])
def guess():
    player_hint = ""
    winning_num = ""
    if request.form['guess']:
        session['num_guesses'] = int(session['num_guesses']) + 1
        if int(request.form['guess']) > session['random_num']:
            player_hint = 'lower'
        elif int(request.form['guess']) < session['random_num']:
            player_hint = 'higher'
        elif int(request.form['guess']) == session['random_num']:
            player_hint = 'match'
            winning_num = session['random_num']
        else:
            player_hint = ""
            winning_num = ""
        if int(session['num_guesses']) == 5 and player_hint != 'match':
            player_hint = 'lose'
            winning_num = session['random_num']
    return render_template('/index.html', hint = player_hint, random_num = winning_num, guesses = session['num_guesses'])

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
