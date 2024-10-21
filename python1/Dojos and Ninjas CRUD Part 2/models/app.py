from flask import Flask, redirect, url_for
from models import Ninja

app = Flask(__name__)

@app.route('/ninjas/<int:ninja_id>/delete')
def delete_ninja(ninja_id):
    ninja = Ninja.query.get(ninja_id)
    ninja.delete()
    return redirect(url_for('dojo_details', dojo_id=ninja.dojo_id))

@app.route('/ninjas/<int:ninja_id>/edit')
def edit_ninja(ninja_id):
    ninja = Ninja.query.get(ninja_id)
    return render_template('ninja_edit.html', ninja=ninja)

@app.route('/ninjas/<int:ninja_id>/update', methods=['POST'])
def update_ninja(ninja_id):
    ninja = Ninja.query.get(ninja_id)
    ninja.update(request.form['name'], request.form['age'])
    return redirect(url_for('dojo_details', dojo_id=ninja.dojo_id))