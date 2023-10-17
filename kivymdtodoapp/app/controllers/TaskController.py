#CLASSES INTERNAS
#-----model------
from app.model.TaskModel import TaskModel
orm_task = TaskModel()
#---------------------

class TaskController:

    @staticmethod
    def create(task_text = str, task_date = str) -> None:
        orm_task.insert(dados = {"task": task_text, "date": task_date})
