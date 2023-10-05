from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder

#classe interna
#from main import Main

class TaskController():
    def POST(self):
        name_task = self.root.ids.name_task.text
        # date = self.root.ids.date_task.text

        # dados = {"name": name,
        #         "desc": desc,
        #         "date": date,
        #         "status": "F"
        #         }
        print(name_task)
        # task = Task()
        # task.createTask(data_p = dados)


# class Task(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

    
#     def build(self):
#         return Builder.load_file("resources/views/create_view.kv")


#     def POSTandCREATE(self) -> None:
#         name = self.root.ids.name_task
#         # desc = self.root.ids.desc_task.text
#         # date = self.root.ids.date_task.text

#         # dados = {"name": name,
#         #         "desc": desc,
#         #         "date": date,
#         #         "status": "F"
#         #         }
#         print(name)
#         # task = Task()
#         # task.createTask(data_p = dados)