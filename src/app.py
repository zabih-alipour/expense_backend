

from flask import Flask, json
import db as db

app = Flask(__name__)


@app.route('/')
def get_current_time():
    return "Home"


@app.route('/subjects')
def get_subjects():
    return json.dumps(db.get_subjects())


@app.route('/invoices')
def get_invoices():
    return json.dumps(db.get_invoices(None))
