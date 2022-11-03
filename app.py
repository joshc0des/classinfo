from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sections.db'
db = SQLAlchemy(app)


class Sections(db.Model):
    crn = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=True)
    course = db.Column(db.String(200), nullable=True)
    section = db.Column(db.String(200), nullable=True)
    section_title = db.Column(db.String(200), nullable=True)
    primary_instructor = db.Column(db.String(200), nullable=True)
    course_dates = db.Column(db.String(200), nullable=True)
    seats_left = db.Column(db.String(200), nullable=True)
    wait_list = db.Column(db.String(200), nullable=True)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Home Page</h1>"


@app.route('/inputs', methods=['GET', 'POST'])
def inputs():
    return render_template('edit.html')


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html')


if __name__ == '__main__':
    app.run()
