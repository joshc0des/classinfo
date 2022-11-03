from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sections.db'
db = SQLAlchemy(app)


class Sections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=True)
    course = db.Column(db.String(200), nullable=True)
    section = db.Column(db.String(200), nullable=True)
    section_title = db.Column(db.String(200), nullable=True)
    primary_instructor = db.Column(db.String(200), nullable=True)
    course_dates = db.Column(db.String(200), nullable=True)
    seats_left = db.Column(db.String(200), nullable=True)
    wait_list = db.Column(db.String(200), nullable=True)


with app.app_context():
    print(1)
    db.create_all()
    print(2)
    print(db)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Home Page</h1>"


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html')


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html')


@app.route('/table', methods=['GET', 'POST'])
def table():
    return render_template('tasks.html')