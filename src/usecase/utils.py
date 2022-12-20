from flask import jsonify
from marshmallow import ValidationError


# handle validation and bad request errors from single source
# all endpoints should be decorated with this function
def request_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as ve:
            return jsonify({"message": ve.messages}), 400
        except RuntimeError:
            return jsonify({"message": "Unknown error occurred"}), 500
    inner_function.__name__ = func.__name__
    return inner_function

