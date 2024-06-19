from flask import Flask, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ecret_key_here' 

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/add_two')
def add_two():
    if 'counter' in session:
        session['counter'] += 2
    else:
        session['counter'] = 2
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    if 'counter' in session:
        session['counter'] = 0
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    increment_by = int(request.form['increment_by'])
    if 'counter' in session:
        session['counter'] += increment_by
    else:
        session['counter'] = increment_by
    return redirect(url_for('index'))

@app.route('/decode_cookie')
def decode_cookie():
    cookie = request.cookies.get('session')
    decoded_cookie = cookie.decode('utf-8')
    return f'Decoded cookie: {decoded_cookie}'

if __name__ == '__main__':
    app.run(debug=True)