from PyQt6 import uic, QtWidgets

class UsuarioController:
    def build(self):
        self.app = QtWidgets.QApplication([])
        self.cadastrar_usuario = uic.loadUi("resources/views/cadastrar_screen.ui")
        self.cadastrar_usuario.show()
        self.cadastrar_usuario.btn_cadastrar.clicked.connect(self.post)
        self.cadastrar_usuario.btn_listar.clicked.connect(self.show)
        return self.app.exec()
    
    def post(self):
        nome = self.cadastrar_usuario.nome.text()
        
        self.cadastrar_usuario.nome.setText("")
        
        print(nome)
        
        
    def show(self):
        self.listar_usuario = uic.loadUi("resources/views/listar_screen.ui")
        
        data = ("nome", "email", "telefone", "matricula")
        
        self.listar_usuario.tableWidget.setRowCount(len(data))
        self.listar_usuario.tableWidget.setColumnCount(4)
        self

        for linha in range(0, len(data)):
            for coluna in range(4):
                 self.listar_usuario.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(data[linha])))
                 print(f"{linha} -> {coluna}")
        
        return self.listar_usuario.show()


#setText("") limpa
#noClicked limpa