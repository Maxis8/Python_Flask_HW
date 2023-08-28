from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(30), nullable=False)
    mark = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('marks', lazy=True))


