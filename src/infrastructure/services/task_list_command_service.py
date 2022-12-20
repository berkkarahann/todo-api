from datetime import datetime

from .task_list_query_service import TaskListQueryService
from ..orm.task_list import TaskList
from src.domain.task_list import task_list_model

task_list_query_service = TaskListQueryService()


# class that encapsulates all write operations for the task list
class TaskListCommandService:
    # creates a new task list
    def create_task_list(self, title: str, user_id: int):
        task_list = TaskList(title=title, user_id=user_id)
        task_list.save()
        return task_list_model.dump(task_list)

    # updates an existing task list
    def update_task_list(
        self,
        task_list_id: int,
        user_id: int,
        title: str
    ):
        task_list = task_list_query_service.find_by_id(task_list_id, user_id,internal_call=True)
        task_list.title = title
        task_list.updated_at = datetime.utcnow()
        task_list.save()
        return task_list_model.dump(task_list)

    # deletes an existing task list
    def delete_task_list_by_id(self, task_list_id: int, user_id: int):
        tasklist = task_list_query_service.find_by_id(task_list_id, user_id,internal_call=True)
        tasklist.deleted_at = tasklist.updated_at = datetime.utcnow()
        tasklist.save()
