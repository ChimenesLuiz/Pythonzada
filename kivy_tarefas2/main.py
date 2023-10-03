#classes externas
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

#classes internas
from app.controllers.CreateScreen import CreateScreen


class Main(MDApp):
    def build(self):
        sm = ScreenManager()
        
        create_screen = CreateScreen(name = 'create_screen')

        sm.add_widget(create_screen.build())

        return sm
    

    def create(self):
        CreateScreen.POSTandCREATE()
        
        
if __name__ == '__main__':
    Main().run() 