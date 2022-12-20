from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from src import db
from src.infrastructure.orm.db_repository import BaseModel


# database model for the user entity
class User(db.Model, BaseModel):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column("username", db.String(64), unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    taskLists = db.relationship("TaskList", backref="user", lazy="dynamic")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<User {self.username}>"

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
