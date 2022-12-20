from src.infrastructure.orm.task_list import TaskList
from src.domain.task_list import task_lists_model, task_list_model


# class that encapsulates all read operations for the task list
class TaskListQueryService:
    # finds an existing task list with given id
    def find_by_id(self, task_list_id: int, user_id: int, internal_call: bool = False):
        try:
            task_list = TaskList.query.filter_by(id=task_list_id, user_id=user_id, deleted_at=None).first_or_404()
        except:
            raise

        return task_list_model.dump(task_list) if not internal_call else task_list

    # finds all task lists of the user
    def find_all(self, user_id: int):
        try:
            task_list = TaskList.query.filter_by(user_id=user_id,deleted_at=None).all()
        except:
            raise

        return task_lists_model.dump(task_list)
