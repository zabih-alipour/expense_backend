import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_current_time():
    return "Home"


@app.route('/subjects')
def get_subjects():
    return "Subjects"

