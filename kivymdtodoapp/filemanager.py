from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView

class FileSaveApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.file_chooser = FileChooserListView()
        save_button = Button(text="Salvar Arquivo")
        save_button.bind(on_release=self.save_file)

        layout.add_widget(save_button)
        layout.add_widget(self.file_chooser)

        return layout

    def save_file(self, instance):
        # Abre a caixa de diálogo de seleção de local para salvar o arquivo
        self.file_chooser.path = '/'  # Pode definir o diretório inicial para a seleção

        # Define a função a ser chamada quando o usuário selecionar o local
        self.file_chooser.bind(on_submit=self.save_to_location)

    def save_to_location(self, instance, selection):
        if selection:
            # O usuário selecionou um local para salvar o arquivo
            selected_location = selection[0]
            file_name = "arquivo.txt"  # Nome do arquivo a ser salvo
            file_path = selected_location + '/' + file_name  # Caminho completo do arquivo\
            print(file_path)
            with open(file_path, 'w') as file:
                file.write("Este é o conteúdo do arquivo que você salvou.")
            print(f"Arquivo salvo em: {file_path}")

if __name__ == '__main__':
    FileSaveApp().run()
