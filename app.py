from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from forms import CourseForm
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = "adg986df7s98h7fg89hsh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sections.db')
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


# # this takes 10159 courses from json and puts them into the db file
# f = open('datatablesdata.json')
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
    form = CourseForm()

    if form.validate_on_submit():
        return redirect(url_for('tasks'))

    return render_template('edit.html', form=form)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    crns = []
    if request.method == "POST":
        crn1 = request.form.get("crn1")
        if len(crn1) == 5:
            crns.append(crn1)

        crn2 = request.form.get("crn2")
        if len(crn2) == 5:
            crns.append(crn2)

        crn3 = request.form.get("crn3")
        if len(crn3) == 5:
            crns.append(crn3)

        crn4 = request.form.get("crn4")
        if len(crn4) == 5:
            crns.append(crn4)

        crn5 = request.form.get("crn5")
        if len(crn5) == 5:
            crns.append(crn5)

        crn6 = request.form.get("crn6")
        if len(crn6) == 5:
            crns.append(crn6)
        print(crns[0])
        print(Sections.query.filter(Sections.crn == crns[0]))

    return render_template('tasks.html')


@app.route('/priceClassesSeats', methods=['GET', 'POST'])
def priceClassesSeats():
    return render_template('priceClassesSeats.html')


@app.route('/numberOfSeats', methods=['GET', 'POST'])
def numberOfSeats():
    return render_template('numberOfSeats.html')
