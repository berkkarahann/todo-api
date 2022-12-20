from datetime import datetime
from src import db
from src.infrastructure.orm.db_repository import BaseModel


# database model for the task-list entity
class TaskList(db.Model, BaseModel):
    __tablename__ = "tasklist"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("title", db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tasks = db.relationship("Task", backref="tasklist", lazy="dynamic")

    def __init__(self, user_id, title=''):
        self.title = title
        self.user_id = user_id
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return f"<Tasklist: {self.title}>"
