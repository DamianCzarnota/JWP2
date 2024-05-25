from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from models import db, Teacher

main = Blueprint('main', __name__)

@main.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    result = []
    for teacher in teachers:
        teacher_data = {
            'id': teacher.id,
            'name': teacher.name,
            'subject': teacher.subject,
            'time': teacher.time
        }
        result.append(teacher_data)
    return jsonify(result)

@main.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        time = request.form['time']
        new_teacher = Teacher(name=name, subject=subject, time=time)
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for('main.get_all_teachers'))

    return render_template('add_teacher.html')

@main.route('/delete_teacher/<int:id>', methods=['POST'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for('main.get_all_teachers'))

@main.route('/all_teachers', methods=['GET'])
def get_all_teachers():
    teachers = Teacher.query.all()
    return render_template('all_teachers.html', teachers=teachers)