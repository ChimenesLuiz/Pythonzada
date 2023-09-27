from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            use_pagination = True,
            check = True,
            column_data=[
                ("Nome", dp(35)),
                ("Descricao", dp(35)),
                ("Data Limite", dp(60)),
                ("Status", dp(35))
            ],
            row_data=[
                (
                    "Passeio",
                    "Passear com meu cachorro rex na praca",
                    "2023/10/10",
                    "A fazer"
                )
            ],
            sorted_on = "Schedule",
            sorted_order = "ASC",
            elevation = 2,
        )
        
        self.data_tables.bind(on_row_press = self.on_row_press)
        self.data_tables.bind(on_check_press = self.on_check_press)
        screen = MDScreen()
        screen.add_widget(self.data_tables)
        return screen

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    # Sorting Methods:
    # since the https://github.com/kivymd/KivyMD/pull/914 request, the
    # sorting method requires you to sort out the indexes of each data value
    # for the support of selections.
    #
    # The most common method to do this is with the use of the builtin function
    # zip and enumerate, see the example below for more info.
    #
    # The result given by these funcitons must be a list in the format of
    # [Indexes, Sorted_Row_Data]

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key = lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key = lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ), 
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))


Example().run()
# from entity.Tarefa import Tarefa

# tk = Tarefa()
# dados = tk.getDados()
# print(dados)