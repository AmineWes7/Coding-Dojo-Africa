from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(flask):
    return f'Hi {flask}!'

@app.route('/repeat/<int:times>/<word>')
def repeat_word(times, word):
    print(f"{times*word}")

if __name__ == '__main__':
    app.run(port=5000)