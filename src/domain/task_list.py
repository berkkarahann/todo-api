from flask_marshmallow.fields import fields
from src import ma


# Task list model for validation and get requests
class TaskListDTO(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


task_list_model = TaskListDTO()
task_lists_model = TaskListDTO(many=True)