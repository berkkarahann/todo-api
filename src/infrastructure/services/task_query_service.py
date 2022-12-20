from src.infrastructure.orm.task import Task
from src.domain.task import task_model, tasks_model


# class that encapsulates all read operations for the task
class TaskQueryService:
    # finds an existing task with given id
    def find_by_id(self, task_list_id: int, task_id: int, user_id: int, internal_call: bool = False):
        try:
            task = Task.query.filter_by(id=task_id, tasklist_id=task_list_id, user_id=user_id,
                                             deleted_at=None).first_or_404()
        except:
            raise

        return task_model.dump(task) if not internal_call else task

    # finds all tasks of the user
    def find_all(self, user_id: int, task_list_id: int):
        try:
            tasks = Task.query.filter_by(user_id=user_id, tasklist_id=task_list_id, deleted_at=None).all()
        except:
            raise

        return tasks_model.dump(tasks)
