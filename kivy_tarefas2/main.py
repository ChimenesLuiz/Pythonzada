from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

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

    
    def on_save(self, instance, value, date_range):
        self.root.ids.date_task.text = str(value)
    
    def on_cancel(self, instance, value):
        """do nothing"""
    
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        MDDatePicker(
            primary_color="blue",
            selector_color="white",
            text_toolbar_color="white",
            text_color="black",
            text_current_color="white",
            text_button_color="blue"
                )
        date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)
        date_dialog.open()
    
    
if __name__ == '__main__':
    Main().run()
