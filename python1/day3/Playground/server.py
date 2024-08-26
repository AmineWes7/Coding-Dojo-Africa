from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html', num_boxes=3, color='blue')

@app.route('/play/<x>')
def play_x(x):
    return render_template('play.html', num_boxes=int(x), color='blue')

@app.route('/play/<x>/<color>')
def play_x_color(x, color):
    return render_template('play.html', num_boxes=int(x), color=color)

if __name__ == '__main__':
    app.run(debug=True)