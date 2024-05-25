from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name}>'