from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe!"

@app.route('/')
def main():
    if 'visits' in session:
        print('key exists!')
        session['visits'] = session['visits'] + 1
    else:
        print("key 'visits' does NOT exist! Creating key...")
        session['visits'] = 1
    if 'user_counter' not in session:
        session['user_counter'] = 0
    return render_template('index.html', visit_count=session['visits'], counter=session['user_counter'])

@app.route('/add_count/<int:inc_num>')
def main2(inc_num):
    if 'visits' in session:
        print('key exists!')
        session['visits'] = session['visits'] + inc_num
    else:
        print("key 'visits' does NOT exist! Creating key...")
        session['visits'] = 1
    return render_template('index.html', visit_count=session['visits'], counter=session['user_counter'])

@app.route('/form_submit', methods=['POST'])
def form_submit():
    if request.form['counter']:
        session['user_counter'] = session['user_counter'] + int(request.form['counter'])
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)