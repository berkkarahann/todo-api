from flask import g, jsonify, request

from src import basic_auth
from src.domain.task import task_model, tasks_model
from src.domain.task_list import task_list_model
from src.infrastructure.services.task_command_service import TaskCommandService
from src.infrastructure.services.task_list_command_service import TaskListCommandService
from src.infrastructure.services.task_list_query_service import TaskListQueryService
from src.infrastructure.services.task_query_service import TaskQueryService
from src.usecase import task_lists_blueprint
from src.usecase.utils import request_handler

# initialize services which are consumed by this use-case
task_query_service = TaskQueryService()
task_list_query_service = TaskListQueryService()
task_command_service = TaskCommandService()
task_list_command_service = TaskListCommandService()


# get task lists of the authenticated user
@task_lists_blueprint.route("/", methods=["GET"])
@basic_auth.login_required
@request_handler
def get_task_lists():
    tasklist = task_list_query_service.find_all(g.user.id)
    return jsonify({"data": tasklist})


# create a new task list for the authenticated user
@task_lists_blueprint.route("/", methods=["POST"])
@basic_auth.login_required
@request_handler
def create_task_list():
    tasklist_input = task_list_model.load(request.get_json())
    task_list = task_list_command_service.create_task_list(
        tasklist_input.get("title"), g.user.id
    )
    return jsonify({"data": task_list}), 201


# update an existing task list which has given id
@task_lists_blueprint.route("/<int:task_list_id>", methods=["PUT"])
@basic_auth.login_required
@request_handler
def update_task_list(task_list_id):
    tasklist_input = task_list_model.load(request.get_json())
    tasklist = task_list_command_service.update_task_list(
        task_list_id, g.user.id, tasklist_input.get("title")
    )
    return jsonify({"data": tasklist}), 200


# delete an existing task list which has given id
@task_lists_blueprint.route("/<int:task_list_id>", methods=["DELETE"])
@basic_auth.login_required
@request_handler
def delete_task_list(task_list_id):
    task_list_command_service.delete_task_list_by_id(task_list_id, g.user.id)
    return jsonify({"message": "Task list is deleted successfully"}), 204


# get all tasks of a given task list of the authenticated user
@task_lists_blueprint.route("/<int:task_list_id>/tasks", methods=["GET"])
@basic_auth.login_required
@request_handler
def get_task(task_list_id):
    tasks = task_query_service.find_all(g.user.id, task_list_id)
    return jsonify({"data": tasks}), 200


# create a new task to the given task list
@task_lists_blueprint.route("/<int:task_list_id>/tasks", methods=["POST"])
@basic_auth.login_required
@request_handler
def create_task(task_list_id):
    task_input = task_model.load(request.get_json())
    task = task_command_service.create_task(
        task_input.get("description"), g.user.id, task_list_id
    )
    return jsonify({"data": task}), 201


# update an existing task which has given id
@task_lists_blueprint.route("/<int:task_list_id>/tasks/<int:task_id>", methods=["PUT"])
@basic_auth.login_required
@request_handler
def update_task(task_list_id, task_id):
    task_input = task_model.load(request.get_json())
    task = task_command_service.update_task(
        task_id,
        task_list_id,
        g.user.id,
        task_input.get("description", None),
        task_input.get("is_finished", False),
    )
    return jsonify({"data": task}), 200


# bulk update for existing tasks
@task_lists_blueprint.route("/<int:task_list_id>/tasks/bulk", methods=["PUT"])
@basic_auth.login_required
@request_handler
def update_tasks(task_list_id):
    tasks_input = tasks_model.load(request.json)
    tasks = task_command_service.update_tasks(tasks_input, task_list_id, g.user.id)
    return jsonify({"data": tasks}), 200


# delete an existing task which has given id
@task_lists_blueprint.route("/<int:task_list_id>/tasks/<int:task_id>", methods=["DELETE"])
@basic_auth.login_required
@request_handler
def delete_task(task_list_id, task_id):
    task_command_service.delete_task_by_id(task_id, task_list_id, g.user.id)
    return jsonify({"message": "Task is deleted successfully"}), 204


# bulk delete for existing tasks
@task_lists_blueprint.route("/<int:task_list_id>/tasks/bulk", methods=["DELETE"])
@basic_auth.login_required
@request_handler
def delete_tasks(task_list_id):
    body = request.get_json()
    task_command_service.delete_tasks(body["task_ids"], task_list_id, g.user.id)
    return jsonify({"message": "Tasks are deleted successfully"}), 204
