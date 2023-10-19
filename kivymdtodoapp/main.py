
#CLASSES EXTERNAS
#-----kivymd------
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
#-----datetime------
from datetime import datetime
#---------------------

#CLASSES INTERNAS
#-----controller------
from app.controllers.TaskController import TaskController
#---------------------

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))
  
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    def __init__(self, pk = None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk

    def check_uncheck(self, check, id):
        if (check.active == True):
            id.text = '[s]' + id.text + '[/s]'
            TaskController.updateMarker(id = str(id.pk), checked = True)
        else:
            data = TaskController.updateMarker(id = str(id.pk), checked = False)
            id.text = str(data[0])

    def delete_task(self, id):
        self.parent.remove_widget(id)
        TaskController.destroy(str(id.pk))

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass

class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        #['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        #self.theme_cls.accent_palette = "Red"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        return Builder.load_file("app/resources/views/main.kv")


    def on_start(self):
        checked_tasks, unchecked_tasks = TaskController.getTasksByMarker()
        self.list_unchecked_tasks(unchecked_tasks = unchecked_tasks)
        self.list_checked_tasks(checked_tasks = checked_tasks)

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )
        self.task_list_dialog.open()

    def show_task_after_add(self, last_id = str):
        data = TaskController.showOne(last_id = last_id)
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk = data[0], text = '[b]'+data[1] + '[/b]', secondary_text = data[2]))

    def list_unchecked_tasks(self, unchecked_tasks = tuple):
        if (len(unchecked_tasks) > 0):
            for task in unchecked_tasks:
                add_task = ListItemWithCheckbox(pk = task[0], text = task[1], secondary_text = task[2])
                add_task.ids.check.active = False
                self.root.ids.container.add_widget(add_task)

    def list_checked_tasks(self, checked_tasks = tuple):
        if (len(checked_tasks) > 0):
            for task in checked_tasks:
                add_task = ListItemWithCheckbox(pk = task[0], text = '[s]' + task[1] + '[/s]', secondary_text = task[2])
                add_task.ids.check.active = True
                self.root.ids.container.add_widget(add_task)

    def add_task(self, task, task_date):
        last_id = TaskController.create(str(task.text), str(task_date))
        task.text = ''
        self.show_task_after_add(last_id = last_id)

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Green" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

if __name__ == '__main__':
    MainApp().run()
