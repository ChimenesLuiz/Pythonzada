from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

#classe interna
from app.controllers.TaskController import TaskController
taskcontroller = TaskController()

class Manager(ScreenManager):
    def build(self):
        sm = Builder.load_file(f"resources/views/views.kv")
        sm.current = 'home'
        return sm

class Home(Screen):
    pass

class CreateTaskScreen(Screen):
    pass
    
class Main(MDApp):
    def build(self):
        return Manager().build()

    def POST(self):
        taskcontroller.POST(ids = self.root.ids)
    
    
if __name__ == '__main__':
    Main().run()
