from flask import Blueprint, jsonify, request
from datetime import datetime

todos_bp = Blueprint('todos', __name__)

todos = []      

# Implement the route functions
@todos_bp.route('/', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to create a new To-Do item
@todos_bp.route('/', methods=['POST'])
def add_todo():
    data = request.json
    new_todo = {
        'id': len(todos) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False,
        'createdAt': datetime.now(),
        'updatedAt': datetime.now()
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Route to get a specific To-Do item
@todos_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    return jsonify(todo) if todo else ('', 404)

# Route to delete a specific To-Do item
@todos_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return ('', 204)

# Route to update a specific To-Do item
@todos_bp.route('/<int:todo_id>', methods=['PUT', 'PATCH'])
def update_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if not todo:
        return ('', 404)

    data = request.json
    todo['title'] = data.get('title', todo['title'])
    todo['description'] = data.get('description', todo['description'])
    todo['completed'] = data.get('completed', todo['completed'])
    todo['updatedAt'] = datetime.now()
    
    return jsonify(todo)