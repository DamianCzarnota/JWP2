from flask import Blueprint, render_template, request, jsonify
from models import Task
from database import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main_bp.route('/add', methods=['POST'])
def add():
    task_content = request.json.get('task')
    if task_content:
        new_task = Task(task=task_content)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'id': new_task.id, 'task': new_task.task}), 201
    return jsonify({'error': 'Invalid input'}), 400

@main_bp.route('/delete/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': 'success'})

@main_bp.route('/edit/<int:task_id>', methods=['PUT'])
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    new_task_content = request.json.get('task')
    if new_task_content:
        task.task = new_task_content
        db.session.commit()
        return jsonify({'id': task.id, 'task': task.task})
    return jsonify({'error': 'Invalid input'}), 400