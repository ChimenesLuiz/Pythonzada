import typing
from PyQt6 import QtCore, uic, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication

#classe interna
from app.model.usuario import Usuario
usuario_model = Usuario()

# from app.controller.iniciocontroller import InicioController

from app.middleware.usuario import UsuarioMiddleware
from app.apis.viacep import Viacep

class UsuarioController(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Cadastro Usuario")
        self.setGeometry(100, 100, 400, 300)
        uic.loadUi("resources/views/cadastrar_usuario_view.ui", self)
        # self.btn_confirmar.clicked.connect(self.post)
        # self.btn_preencher_cep.clicked.connect(self.preencher_cep)
        # self.btn_voltar.clicked.connect(self.voltar)
        
    # def build(self):
    #     self.show()
    
    # def post(self):
    #     #validacoes
        
    #     if (UsuarioMiddleware.verificaEmail(self.cadastrar_usuario.email.text()) == True
    #         and
    #         UsuarioMiddleware.verificaTelefone(self.cadastrar_usuario.telefone.text()) == True
    #         and
    #         UsuarioMiddleware.verificaCpf(self.cadastrar_usuario.cpf.text()) == True
    #         and
    #         type(Viacep.getCep(self.cadastrar_usuario.cep.text())) == dict):


    #         usuario_model.cadastrar({"nome": self.cadastrar_usuario.nome.text(),
    #                                 "email": self.cadastrar_usuario.email.text(),
    #                                 "telefone": self.cadastrar_usuario.telefone.text(),
    #                                 "cpf": self.cadastrar_usuario.cpf.text(),
    #                                 "cep": self.cadastrar_usuario.cep.text(),
    #                                 "endereco": self.cadastrar_usuario.endereco.text(),
    #                                 "numero": self.cadastrar_usuario.numero.text(),
    #                                 "bairro": self.cadastrar_usuario.bairro.text()
    #                                 })
    #         self.cadastrar_usuario.nome.setText("")
    #         self.cadastrar_usuario.email.setText("")
    #         self.cadastrar_usuario.telefone.setText("")
    #         self.cadastrar_usuario.cpf.setText("")
    #         self.cadastrar_usuario.cep.setText("")
    #         self.cadastrar_usuario.endereco.setText("")
    #         self.cadastrar_usuario.numero.setText("")
    #         self.cadastrar_usuario.bairro.setText("")

    #         # self.showData()
    #     else:
    #         print('erro')

              
    # def showData(self):

        
    #     data = usuario_model.getDados()
        
    #     if (data):
    #         self.cadastrar_usuario.tableWidget.setRowCount(len(data))
    #         self.cadastrar_usuario.tableWidget.setColumnCount(len(data[0]))

    #         self.cadastrar_usuario.tableWidget.setHorizontalHeaderLabels(('ID', 'NOME', 'EMAIL', 'TELEFONE', 'CPF', 'CEP', 'ENDERECO', 'NUMERO', 'BAIRRO'))
    #         for linha in range(len(data)):
    #             for coluna in range(len(data[0])):
    #                 self.cadastrar_usuario.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(data[linha][coluna])))
            
    #         return self.cadastrar_usuario.show()
    #     else:
    #         print('nao existem dados')

    # def preencher_cep(self):
    #     dados_cep = Viacep.getCep(self.cadastrar_usuario.cep.text())
    #     self.cadastrar_usuario.endereco.setText(dados_cep["logradouro"])
    #     self.cadastrar_usuario.bairro.setText(dados_cep["bairro"])

    # def voltar(self):
    #     self.close()