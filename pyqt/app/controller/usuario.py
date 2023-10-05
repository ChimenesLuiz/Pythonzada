import typing
from PyQt6 import QtCore, uic, QtWidgets

#classe interna
from app.model.usuario import Usuario
usuario_objeto = Usuario()

class UsuarioController():


    def build(self):
        self.app = QtWidgets.QApplication([])
        self.cadastrar_usuario = uic.loadUi("resources/views/cadastrar_screen.ui")
        self.cadastrar_usuario.show()
        self.cadastrar_usuario.btn_cadastrar.clicked.connect(self.post)
        #self.cadastrar_usuario.btn_listar.clicked.connect(self.show)

        self.show()
        return self.app.exec()
    
    def post(self):
        nome = self.cadastrar_usuario.nome.text()
        email = self.cadastrar_usuario.email.text()
        telefone = self.cadastrar_usuario.telefone.text()
        matricula = self.cadastrar_usuario.matricula.text()
        
        self.cadastrar_usuario.nome.setText("")
        self.cadastrar_usuario.email.setText("")
        self.cadastrar_usuario.telefone.setText("")
        self.cadastrar_usuario.matricula.setText("")

        
        #print(nome, email, telefone, matricula)
        usuario_objeto.cadastrar({"matricula": matricula, "nome": nome, "email": email, "telefone": telefone})
        self.show()

        
        
    def show(self):

        #self.listar_usuario = uic.loadUi("resources/views/cadastrar_screen.ui")
        
        data = usuario_objeto.getDados()
        
        self.cadastrar_usuario.tableWidget.setRowCount(len(data))
        self.cadastrar_usuario.tableWidget.setColumnCount(len(data[0]))

        self.cadastrar_usuario.tableWidget.setHorizontalHeaderLabels(('Matricula', 'Nome', 'Email', 'Telefone'))

        for linha in range(len(data)):
            for coluna in range(len(data[0])):
                 self.cadastrar_usuario.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(data[linha][coluna])))
                 print(f"{linha} -> {coluna}")
        
        return self.cadastrar_usuario.show()


#setText("") limpa
#noClicked limpa