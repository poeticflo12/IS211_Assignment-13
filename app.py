import json
import re

from flask import Flask, render_template, request, flash, redirect,url_for
from flask_login import LoginManager,current_user, login_user, login_required,logout_user

import sqlite3
from sqlite3 import Error
from flask_sqlalchemy import SQLAlchemy
from models.StudentMarks import StudentMarks
from models.Student import Student
from models.Quizzes import Quizzes
import os
from flask_migrate import Migrate
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'f3cfe9ed8fae309f02079dbf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'hw13.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


login = LoginManager(app)
login.login_view = 'login'

# from models.Test import Test
from models import User
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
db.create_all()
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session

# Base = automap_base()
# Base.prepare(db.engine, reflect=True)

# Users = Base.classes.users
# session = Session(db.engine)
@login.user_loader
def load_user(id):
    return User.User.query.get(id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        #get data

        username=request.form['username']
        password=request.form['password']

        user = User.User.query.filter_by(username=username).first()
        if user is None:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, False)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def index():
    student_results=StudentMarks().viewall()
    students=Student().view_all_students()
    quizzes= Quizzes().view_all_quizzes()
    # return json.dumps(quizzes)
    return render_template('index.html', student_results=student_results,students=students, quizzes=quizzes)

@app.route("/student", methods=['get','post'])
@login_required
def student():
    if request.method=="POST":
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        # return firstname
        add_student=Student([firstname,lastname]).addStudent()
        return redirect(url_for("index"))


@app.route("/student/add")
def add_student():
    return render_template('student.html')

@app.route('/student/delete/<id>')
@login_required
def delele_student(id):
    Student().delete_student(id)
    return redirect(url_for("index"))

@app.route('/quiz/add',methods=['get','post'])
@login_required
def quiz():
    if request.method=="POST":
        subject=request.form['subject']
        question=request.form['questions']
        date=request.form['date']
        add_subject=Quizzes([subject,question,date]).add_quiz()
        return redirect(url_for('index'))
    return render_template('quiz.html')

@app.route('/quiz/delete/<id>')
@login_required
def delele_quiz(id):
    Quizzes().delete_quiz(id)
    return redirect(url_for("index"))

@app.route('/marks/delete/<id>')
@login_required
def delele_marks(id):
    StudentMarks().delete_marks(id)
    return redirect(url_for("index"))


@app.route('/marks',methods=['get','post'])
@login_required
def marks():
    if request.method=="POST":
        subject=request.form['subject']
        student=request.form['student']
        marks=int(request.form['marks'])
        # return subject
        add_subject=StudentMarks([marks,student,subject]).addmarks()
        return redirect(url_for('index'))

@app.route('/student/<id>',methods=['get'])
def view_result(id):
    result=StudentMarks().single_student(id)
    # return json.dumps(result)
    return render_template('studentmarks.html', result=result)

@app.route('/results/add',methods=['get','post'])
@login_required
def add_results():
    students=Student().view_all_students()
    quizzes= Quizzes().view_all_quizzes()
    return render_template('marks.html',students=students, quizzes=quizzes)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)