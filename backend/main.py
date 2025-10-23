from config import app, db
from flask import jsonify, request
from models import to_do

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = to_do.query.all()
    json_todos = list(map(lambda x: x.to_json(), todos))
    return jsonify({'to_do': json_todos}), 200

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)