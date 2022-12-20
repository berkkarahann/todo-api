from flask_marshmallow.fields import fields
from src import ma

# Task model for validation and get requests
class TaskDTO(ma.Schema):
    id = fields.Integer()
    description = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    finished_at = fields.DateTime()
    is_finished = fields.Boolean()


task_model = TaskDTO()
tasks_model = TaskDTO(many=True)
