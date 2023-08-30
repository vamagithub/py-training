from flask import request, redirect, url_for, render_template, jsonify

from app import app, db
from app.models import Student, Teacher

@app.route("/", methods=["GET"])
def home_student():
    return render_template("home.html")


@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        physics = request.form.get("physics")
        maths = request.form.get("maths")
        english = request.form.get("english")
        student = Student(
            name=name,
            age=age,
            physics=physics,
            maths=maths,
            english=english
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('student', student_id=student.id))
    return render_template("insert.html")


@app.route("/student/<student_id>", methods=["GET"])
def student(student_id):
    student = Student.query.get(int(student_id))
    return render_template("student.html", student=student)



@app.route("/t", methods=["GET"])
def home_teacher():
    return render_template("teacher_home.html")

@app.route("/t-insert", methods = ["GET", "POST"])
def teacher_insert():

    if request.method == "POST":
        name = request.form.get('name')
        subject = request.form.get('subject')
        teacher = Teacher(
            name = name,
            subject = subject
        )
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('teacher', teacher_id = teacher.id))
    return render_template("teacher_insert.html")


@app.route("/teacher/<teacher_id>", methods=["GET"])
def teacher(teacher_id):
    teacher = Teacher.query.get(int(teacher_id))
    return render_template('teacher.html', teacher = teacher)