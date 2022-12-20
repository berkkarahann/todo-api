from datetime import datetime
from src import db
from src.infrastructure.orm.db_repository import BaseModel


# database model for the task entity
class Task(db.Model, BaseModel):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime, index=True)
    is_finished = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tasklist_id = db.Column(db.Integer, db.ForeignKey("tasklist.id"))

    def __init__(self, description, tasklist_id, user_id):
        self.description = description
        self.tasklist_id = tasklist_id
        self.user_id = user_id
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Task: {} by {}>".format(
            self.description, self.user_id or "None"
        )
