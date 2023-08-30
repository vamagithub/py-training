from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    physics = db.Column(db.Integer)
    maths = db.Column(db.Integer)
    english = db.Column(db.Integer)

    def __repr__(self):
        return "<User {}>".format(self.name)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    subject = db.Column(db.String(64))

    def __repr__(self):
        return f"<Teacher - {self.name}>"