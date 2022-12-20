from flask import request, jsonify

from src.domain.user import user_model
from src.usecase import auth_blueprint
from src.usecase.utils import request_handler

from src.infrastructure.services.user_command_service import UserCommandUseCase

user_command_service = UserCommandUseCase()

# logging in with provided username and password
@auth_blueprint.route("/login", methods=["POST"])
@request_handler
def login():
    user_input = user_model.load(request.get_json())
    result = user_command_service.login(user_input.get("username"), user_input.get("password"))
    if result:
        return jsonify({"message": "Successful login"}), 200
    return jsonify({"message": "Unknown username or wrong password"}), 400


# registering a new user with username and password
@auth_blueprint.route("/register", methods=["POST"])
@request_handler
def register():
    user_input = user_model.load(request.get_json())
    result = user_command_service.register(user_input.get("username"), user_input.get("password"))
    if result:
        return jsonify({"message": "User is created successfully"}), 201
    return jsonify({"message": "username has already been taken"}), 400
