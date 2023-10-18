#CLASSES INTERNAS
#-----model------
from app.model.TaskModel import TaskModel
orm_task = TaskModel()
#---------------------

class TaskController:

    @staticmethod
    def create(task_text = str, task_date = str) -> None:
        last_id = orm_task.insertWithLastID(dados = {"task": task_text, "date": task_date})
        return str(last_id)
        
    @staticmethod
    def showOne(last_id = str) -> None:
        data = orm_task.selectByID(id = last_id)
        return data
    
    @staticmethod
    def show() -> None:
        data = orm_task.select()
        return data
    
    @staticmethod
    def destroy(id = str) -> None:
        orm_task.deleteByID(id = id)

    @staticmethod
    def updateMarker(id = str, checked = bool) -> None:
        if (checked == True):
            orm_task.updateMarkerChecked(id = id)
        else:
            orm_task.updateMarkerUnchecked(id = id)