
#CLASSES EXTERNAS
#-----kivymd------
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
#-----datetime------
from datetime import datetime
#---------------------

#CLASSES INTERNAS
#-----controller------
from app.controllers.TaskController import TaskController
#---------------------



class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX THAT GETS THE TASK FROM THE USER"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    
    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

# After creating the database.py
class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk

    # def mark(self, check, the_list_item):
    #     '''mark the task as complete or incomplete'''
    #     if check.active == True:
    #         the_list_item.text = '[s]'+the_list_item.text+'[/s]'
    #         db.mark_task_as_complete(the_list_item.pk)# here
    #     else:
    #         the_list_item.text = str(db.mark_task_as_incomplete(the_list_item.pk))# Here

    def delete_task(self, id):
        self.parent.remove_widget(id)
        TaskController.destroy(str(id.pk))

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''

# Main App class
class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )

        self.task_list_dialog.open()

    def show(self):
        data = TaskController.show()
        for task in data:
            add_task = ListItemWithCheckbox(pk = task[0], text = task[1], secondary_text = task[2])
            self.root.ids.container.add_widget(add_task)

    def on_start(self):
        self.show()
        # # Load the saved tasks and add them to the MDList widget when the application starts
        # try:
        #     completed_tasks, incompleted_tasks = db.get_tasks()

        #     if incompleted_tasks != []:
        #         for task in incompleted_tasks:
        #             add_task = ListItemWithCheckbox(pk=task[0],text=task[1], secondary_text=task[2])
        #             self.root.ids.container.add_widget(add_task)

        #     if completed_tasks != []:
        #         for task in completed_tasks:
        #             add_task = ListItemWithCheckbox(pk=task[0],text='[s]'+task[1]+'[/s]', secondary_text=task[2])
        #             add_task.ids.check.active = True
        #             self.root.ids.container.add_widget(add_task)
        # except Exception as e:
        #     print(e)
        #     pass

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def show_task_after_add(self, last_id = str):
        data = TaskController.showOne(last_id = last_id)
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk = data[0], text = '[b]'+data[1] + '[/b]', secondary_text = data[2]))

    def add_task(self, task, task_date):
        last_id = TaskController.create(str(task.text), str(task_date))
        task.text = ''
        self.show_task_after_add(last_id = last_id)

if __name__ == '__main__':
    app = MainApp()
    app.run()
