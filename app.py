from random import randint
from flask import Flask,render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test1')
def test1():  # put application's code here
    return render_template('test1.html')

@app.route('/sessions')
def sessions():  # put application's code here
    data = {"session_count": randint(1,100)}
    return jsonify(data)




if __name__ == '__main__':
    app.run()
