#CLASSES INTERNAS
#-----model------
from app.model.TaskModel import TaskModel
orm_task = TaskModel()
#---------------------

class TaskController:

    @staticmethod
    def create(task_text = str, task_date = str) -> str:
        last_id = orm_task.insertWithLastID(dados = {"task": task_text, "date": task_date})
        return str(last_id)
        
    @staticmethod
    def show() -> tuple:
        data = orm_task.select()
        return data
    
    @staticmethod
    def getTasksByMarker() -> tuple or list:
        data = TaskController.show()

        checked_tasks = []
        unchecked_tasks = []

        for task in data:
            #SE O CAMPO COMPLETED NA TABELA FOR IGUAL A 1
            #IF COMPLETED COLUMN EQUALS TO 1
            if (task[3] == 1):
                checked_tasks.append(task)
            else:
                unchecked_tasks.append(task)

        return checked_tasks, unchecked_tasks

    @staticmethod
    def showOne(last_id = str) -> tuple:
        data = orm_task.selectByID(id = last_id)
        return data
       
    @staticmethod
    def updateMarker(id = str, checked = bool) -> None or tuple:
        if (checked == True):
            orm_task.updateMarkerChecked(id = id)
        else:
            return orm_task.updateMarkerUnchecked(id = id)

    @staticmethod
    def destroy(id = str) -> None:
        orm_task.deleteByID(id = id)
