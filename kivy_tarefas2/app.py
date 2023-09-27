from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

KV = '''
MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDRaisedButton:
                    on_press: Main.POST()
                    text: "Cadastrar"
                    md_bg_color: "green"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    
                    
                MDTextField:
                    id: data
                    hint_text: "Data para conclusao"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .55}
                    size_hint_x: .5
                    
                MDTextField:
                    id: descricao
                    hint_text: "Descricao"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    size_hint_x: .5
                    
                MDTextField:
                    id: nome_tarefa
                    hint_text: "Nome Tarefa"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: .5
                
                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
'''


class ContentNavigationDrawer(MDBoxLayout):
    pass
#self.root.ids.$variavel

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    
    def POST(self):
        dados = {"nome": self.root.ids.nome_tarefa,
                "descricao": self.root.ids.descricao,
                "data_tarefa": self.root.ids.data_tarefa,
                "estado_tarefa": "F"}

        print(dados)
    


Main().run()