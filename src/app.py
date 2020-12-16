from flask import Flask, json, request
import db as db

app = Flask(__name__)


@app.route('/')
def get_current_time():
    return "Home"


@app.route('/subjects')
def get_subjects():
    return json.dumps(db.get_subjects())


@app.route('/subjects', methods=['POST'])
def add_subject():
    subject = request.get_json()
    return json.dumps(db.add_subject(subject))


@app.route('/subjects/<string:name>')
def get_subject_by_name(name):
    return json.dumps(db.get_subject_by_name(name))


@app.route('/invoices')
def get_invoices():
    return json.dumps(db.get_invoices(None))


@app.route('/invoices', methods=['POST'])
def add_invoice():
    invoice = request.get_json()
    return json.dumps(db.add_invoice(invoice))


@app.route('/invoices/<int:subject_id>')
def get_invoices_by_subject(subject_id):
    return json.dumps(db.get_invoices(subject_id))


@app.route('/reports/daily-expense')
def report_daily_expense():
    return json.dumps(db.get_daily_expense())


@app.route('/reports/subject-expense')
def report_subject_expense():
    return json.dumps(db.get_subject_expense())
