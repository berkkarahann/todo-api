from typing import Optional

from flask import g
from sqlalchemy.exc import NoResultFound

from src import basic_auth
from src.infrastructure.orm.user import User


# class that encapsulates all read operations for the user
class UserQueryService:
    # handles basic auth for the endpoints that are secured
    @staticmethod
    @basic_auth.verify_password
    def verify_password(username: str, password: str):
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return False
        g.user = user
        return True

    # finds an existing user by username
    def find_by_username(self, username: str) -> Optional[User]:
        try:
            existing_user = User.query.filter_by(username=username).one()
        except NoResultFound:
            return None
        except:
            raise

        return existing_user
