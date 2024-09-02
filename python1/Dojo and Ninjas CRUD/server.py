from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Connection Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DATABASE'] = 'dojos_and_ninjas_schema'

# Create a MySQL connection
db = mysql.connector.connect(**app.config)
cursor = db.cursor()

# Routes

@app.route('/')
@app.route('/dojos')
def dojos():
    cursor.execute("SELECT * FROM dojos")
    dojos = cursor.fetchall()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    cursor.execute("SELECT * FROM dojos WHERE id = %s", (dojo_id,))
    dojo = cursor.fetchone()  
    cursor.execute("SELECT * FROM ninjas WHERE dojo_id = %s", (dojo_id,))
    ninjas = cursor.fetchall()
    return render_template('dojo_show.html', dojo=dojo, ninjas=ninjas)

@app.route('/new_dojo', methods=['POST', 'GET'])
def new_dojo():
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("INSERT INTO dojos (name) VALUES (%s)", (name,))
        db.commit()
        return redirect(url_for('dojos'))
    return render_template('new_dojo.html')

@app.route('/new_ninja', methods=['POST', 'GET'])
def new_ninja():
    cursor.execute("SELECT * FROM dojos")
    dojos = cursor.fetchall()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        dojo_id = request.form['dojo_id']
        cursor.execute("INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%s, %s, %s, %s)", 
                    (first_name, last_name, age, dojo_id))
        db.commit()
        return redirect(url_for('dojos'))
    return render_template('new_ninja.html', dojos=dojos)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)