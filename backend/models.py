from config import db

class to_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=False)
    completed = db.Column(db.Boolean, unique=False, nullable=False)
    due_date = db.Column(db.String(20), unique=False, nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'due_date': self.due_date
        }
