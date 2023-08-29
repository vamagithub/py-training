from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    physics = db.Column(db.Integer)
    maths = db.Column(db.Integer)
    english = db.Column(db.Integer)

    def __repr__(self):
        return "<Student {}>".format(self.name)

    @property
    def total(self):
        return self.physics + self.maths + self.english
