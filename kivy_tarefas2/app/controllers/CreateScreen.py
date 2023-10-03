from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder

from app.model.task import Task

class CreateScreen(Screen, MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    def build(self):
        return Builder.load_file("resources/views/create.kv")


    def POSTandCREATE(self) -> None:
        name = self.root.ids.name_task.text
        desc = self.root.ids.desc_task.text
        date = self.root.ids.date_task.text

        dados = {"name": name,
                "desc": desc,
                "date": date,
                "status": "F"
                }
        task = Task()
        task.createTask(data_p = dados)