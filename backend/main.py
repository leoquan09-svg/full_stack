from config import app, db
from flask import jsonify, request
from models import to_do

#Retrive all existing to-do items
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = to_do.query.all()
    json_todos = list(map(lambda x: x.to_json(), todos))
    return jsonify({'to_do': json_todos}), 200

#create a new to-do item
@app.route('/create_todo', methods=['POST'])
def create_todo():
    title = request.json.get('title')
    description = request.json.get('description')
    completed = request.json.get('completed', False)
    due_date = request.json.get('due_date')

    new_todo = to_do(title=title, description=description, completed=completed, due_date=due_date)

    try:
        db.session.add(new_todo)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify('Message: To-Do created successfully!'), 201

#edit an existing to-do item
@app.route('/update_todo/<int:id>')
def update_todo(id, methods=['PATCH']):
    todo = to_do.query.get(id)

    if not todo:
        return jsonify({'error': 'To-Do not found!'}), 404
    
    data = request.json
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    todo.due_date = data.get('due_date', todo.due_date)

    db.session.commit()
    return jsonify('Message: To-Do updated successfully!'), 200

#delete a to-do item
@app.route('/delete_todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = to_do.query.get(id)

    if not todo:
        return jsonify({'error': 'To-Do not found!'}), 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify('Message: To-Do deleted successfully!'), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)