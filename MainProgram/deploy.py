import pickle
from flask import Flask, abort, jsonify, request
import Start
import os
app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


@app.route('/api', methods=['GET'])
def get_number():
    name = '/home/sarthak/Desktop/car6.mp4'
    os.system("python /home/sarthak/Desktop/ALPR/MainProgram/Start.py")
    return "hello"


if __name__ == '__main__':
    app.run(port=8790,  debug=True)
