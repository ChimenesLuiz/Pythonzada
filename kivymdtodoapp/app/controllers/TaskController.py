#CLASSES EXTERNAS
#-----shutil------
import shutil
#---------------------
#CLASSES INTERNAS
#-----model------
from app.model.TaskModel import TaskModel
orm_task = TaskModel()
#-----controllers------
from app.controllers.DirectoryController import DirectoryController
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
    def getOrderTasks() -> tuple or list:
        data = orm_task.orderByTaskSelect()
        return data

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

    #OTHERS
    @staticmethod
    def export() -> None:
        so = DirectoryController.getSO()
        if (so == "Linux"):
            orm_task.export_sql()
            return DirectoryController.createInLinux()
        if (so == "Windows"):
            return DirectoryController.createInWindows()
        if (so == "Android"):
            return DirectoryController.createInAndroid()
        
    @staticmethod
    def import_sql(file = str) -> None:
        DirectoryController.rmDb()
        orm_task.import_sql(file = file)