from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment_by_2')
def increment_by_2():
    session['counter'] += 2
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect(url_for('index'))

@app.route('/increment_by', methods=['POST'])
def increment_by():
    increment = int(request.form['increment'])
    session['counter'] += increment
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)