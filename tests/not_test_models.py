from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import models
from config import TestConfig


def test_student_model():
    student = models.Student(
        name='Testing1',
        age=200,
        physics=90,
        maths=80,
        english=100
    )

    assert student.total == 270
    assert repr(student) == f'<Student Testing1>'

