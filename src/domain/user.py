from flask_marshmallow.fields import fields
from src import ma


# User model for validation and get requests
class User(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


user_model = User()
