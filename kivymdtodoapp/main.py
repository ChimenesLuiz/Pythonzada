
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
from kivymd.uix.button import MDFlatButton
from plyer import filechooser 
#-----datetime------
from datetime import datetime
#---------------------

#CLASSES INTERNAS
#-----controller------
from app.controllers.TaskController import TaskController
#---------------------

class GetIds(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        tasks = TaskController.getOrderTasks()
        self.list_tasks(tasks = tasks)

    def show_task_dialog(self):
        if (not self.task_list_dialog):
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )
        self.task_list_dialog.open()

    def show_export_dialog(self, exported_at = ""):
        if (not self.task_list_dialog):
            self.export_dialog = MDDialog(
                title = f"Exported at {exported_at}",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.close_export_dialog
                    )
                ]

            )
        self.export_dialog.open()

    def show_task_after_add(self, last_id = str):
        data = TaskController.showOne(last_id = last_id)
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk = data[0], text = '[b]'+data[1] + '[/b]', secondary_text = data[2]))

    def list_tasks(self, tasks = tuple):
        if (len(tasks) > 0):
            for task in tasks:
                if (task[3] == False):
                    add_task = ListItemWithCheckbox(pk = task[0], text = task[1], secondary_text = task[2])
                    add_task.ids.check.active = False
                    self.root.ids.container.add_widget(add_task)
                else:
                    add_task = ListItemWithCheckbox(pk = task[0], text = '[s]' + task[1] + '[/s]', secondary_text = task[2])
                    add_task.ids.check.active = True
                    self.root.ids.container.add_widget(add_task)

    def refresh_tasks(self):
        self.root.ids.container.clear_widgets()
        self.on_start()

    def add_task(self, task, task_date):
        last_id = TaskController.create(str(task.text), str(task_date))
        task.text = ''
        self.show_task_after_add(last_id = last_id)

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()
        self.task_list_dialog = None

    def close_export_dialog(self, *args):
        self.export_dialog.dismiss()
        self.task_list_dialog = None

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Green" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def export_data_tasks(self):
        exported_at = TaskController.export()
        self.show_export_dialog(exported_at = exported_at)

    def choose_file_to_import(self):
        filechooser.open_file(on_selection = self.import_data_tasks)
    
    def import_data_tasks(self, selection):
        TaskController.import_sql(file = selection[0])
        self.on_start()
    


if __name__ == '__main__':
    MainApp().run()
