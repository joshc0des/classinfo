from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sections.db'
db = SQLAlchemy(app)


class Sections(db.Model):
    current_row_on_page = db.Column(db.Integer, nullable=True)
    crn = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=True)
    course = db.Column(db.String(200), nullable=True)
    section = db.Column(db.String(200), nullable=True)
    section_title = db.Column(db.String(200), nullable=True)
    primary_instructor = db.Column(db.String(200), nullable=True)
    course_dates = db.Column(db.String(200), nullable=True)
    seats_left = db.Column(db.String(200), nullable=True)
    wait_list = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Class CRN {self.crn}>'


# f = open('datatablesdata.json')
# # this takes 10159 courses from json and puts them into the db file
# data = json.load(f)
# with app.app_context():
#     db.drop_all()
#     db.create_all()
#
#     for course in data["data"]:
#         c = Sections(**course)
#         db.session.add(c)
#         db.session.commit()
#
#     print(len(Sections.query.all()))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('edit'))
    return render_template('home.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        return redirect(url_for('tasks'))
    return render_template('edit.html')


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html')


@app.route('/table', methods=['GET', 'POST'])
def table():
    return render_template('tasks.html')
