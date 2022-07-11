from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Supercalifragilisticexpialidocious!"

@app.route('/')
def main():
    if 'random_num' not in session:
        print("Generating and storing random number...")
        session['random_num'] = random.randint(1, 100)
    return render_template('index.html', hint="", random_num="")

@app.route('/guess', methods=['POST'])
def guess():
    player_hint = ""
    winning_num = ""
    if request.form['guess']:
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
    return render_template('/index.html', hint = player_hint, random_num = winning_num)

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
