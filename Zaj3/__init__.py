from flask import Flask
from config import Config
from models import db, Teacher
from routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        if not Teacher.query.first():  # Dodaj nauczycieli tylko jeśli baza jest pusta
            teacher1 = Teacher(name="John Doe", subject="Mathematics", time="09:00-10:00")
            teacher2 = Teacher(name="Jane Smith", subject="Physics", time="10:00-11:00")
            teacher3 = Teacher(name="Emily Davis", subject="Chemistry", time="11:00-12:00")
            db.session.add_all([teacher1, teacher2, teacher3])
            db.session.commit()

    return app