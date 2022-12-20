from datetime import datetime
from typing import List

from src.infrastructure.orm.task import Task
from src.domain.task import task_model, tasks_model
from .task_query_service import TaskQueryService

task_query_service = TaskQueryService()


# class that encapsulates all write operations for the task
class TaskCommandService:
    # creates a new task
    def create_task(self, description: str, user_id: int, task_list_id: int):
        task = Task(description=description, user_id=user_id, tasklist_id=task_list_id)
        task.save()
        return task_model.dump(task)

    # updates an existing task
    def update_task(
        self,
        task_id: int,
        task_list_id: int,
        user_id: int,
        description: str = None,
        is_finished: bool = False,
    ):
        task = task_query_service.find_by_id(
            task_list_id, task_id, user_id, internal_call=True
        )
        if description:
            task.description = description
        if is_finished:
            task.is_finished = is_finished
            task.finished_at = datetime.utcnow()
        task.updated_at = datetime.utcnow()
        task.save()
        return task_model.dump(task)

    # updates multiple tasks
    def update_tasks(self, tasks: tasks_model, task_list_id: int, user_id: int):
        updated_tasks = []
        for task in tasks:
            updated_tasks.append(
                self.update_task(
                    task["id"],
                    task_list_id,
                    user_id,
                    task.get("description", None),
                    task.get("is_finished", False),
                )
            )

        return updated_tasks

    # deletes an existing task
    def delete_task_by_id(self, task_id: int, task_list_id: int, user_id: int):
        task = task_query_service.find_by_id(
            task_list_id, task_id, user_id, internal_call=True
        )
        task.deleted_at = task.updated_at = datetime.utcnow()
        task.save()

    # deletes multiple tasks
    def delete_tasks(self, task_ids: List[int], task_list_id: int, user_id: int):
        for task_id in task_ids:
            self.delete_task_by_id(task_id, task_list_id, user_id)
