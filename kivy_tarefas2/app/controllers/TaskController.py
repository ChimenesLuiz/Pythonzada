from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder

#classe interna
from app.model.task import Task


class TaskController(MDApp):
    def POST(self, ids):

        dados = {"name": ids.name_task.text,
                "desc": ids.desc_task.text,
                "date": ids.date_task.text,
                "status": "F"
                }

        task = Task()
        task.insertTask(data_p = dados)
