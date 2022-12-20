from flask import Blueprint

auth_blueprint = Blueprint("auth", __name__)

from . import user_usecase

task_lists_blueprint = Blueprint("task-lists", __name__)

from . import task_lists_usecase
