from flask import request, redirect, url_for, render_template, jsonify

from app import app, db
from app.models import Student


@app.route("/", methods=["GET"])
def home():
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
