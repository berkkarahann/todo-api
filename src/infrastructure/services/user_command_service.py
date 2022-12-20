from typing import Optional

from .task_query_service import TaskQueryService
from .user_query_service import UserQueryService
from ..orm.user import User

# initialize query services which are consumed in write operations internally
task_query_service = TaskQueryService()
user_query_service = UserQueryService()


# class that encapsulates all operations for the user
class UserCommandUseCase:
    # manages log-in operation
    def login(self, username: str, password: str) -> Optional[bool]:
        user = user_query_service.find_by_username(username)
        if user and user.verify_password(password):
            return True
        return False

    # creates a new user if given username does not exist
    def register(
        self,
        username: str, password: str
    ) -> Optional[bool]:
        existing_user = user_query_service.find_by_username(username)
        if existing_user:
            return False
        user = User(username=username)
        user.hash_password(password)
        user.save()
        return True
