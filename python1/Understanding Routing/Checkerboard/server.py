from flask import Flask, render_template, request

app = Flask(__name__)

# Root route
@app.route('/')
def index():
    return render_template('checkerboard.html', rows=8, cols=8)

# Route with single parameter
@app.route('/<int:x>')
def single_param(x):
    return render_template('checkerboard.html', rows=x, cols=8)

# NINJA BONUS: Route with two parameters
@app.route('/<int:x>/<int:y>')
def two_params(x, y):
    return render_template('checkerboard.html', rows=x, cols=y)

# SENSEI BONUS: Route with four parameters
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def four_params(x, y, color1, color2):
    return render_template('checkerboard.html', rows=x, cols=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)