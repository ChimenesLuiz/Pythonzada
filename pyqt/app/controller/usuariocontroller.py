import typing
from PyQt6 import QtCore, uic, QtWidgets

#classe interna
from app.model.usuario import Usuario
usuario_model = Usuario()

from app.middleware.usuario import UsuarioMiddleware
from app.apis.viacep import Viacep

class UsuarioController():

    def build(self):
        self.app = QtWidgets.QApplication([])
        self.cadastrar_usuario = uic.loadUi("resources/views/cadastrar_usuario_view.ui")
        self.cadastrar_usuario.show()
        self.cadastrar_usuario.btn_confirmar.clicked.connect(self.post)
        self.cadastrar_usuario.btn_preencher_cep.clicked.connect(self.preencher_cep)
        self.cadastrar_usuario.btn_voltar.clicked.connect(self.voltar)

        self.show()
        return self.app.exec()
    

    def post(self):
        #validacoes
        
        if (UsuarioMiddleware.verificaEmail(self.cadastrar_usuario.email.text()) == True
            and
            UsuarioMiddleware.verificaTelefone(self.cadastrar_usuario.telefone.text()) == True
            and
            UsuarioMiddleware.verificaCpf(self.cadastrar_usuario.cpf.text()) == True
            and
            type(Viacep.getCep(self.cadastrar_usuario.cep.text())) == dict):


            usuario_model.cadastrar({"nome": self.cadastrar_usuario.nome.text(),
                                    "email": self.cadastrar_usuario.email.text(),
                                    "telefone": self.cadastrar_usuario.telefone.text(),
                                    "cpf": self.cadastrar_usuario.cpf.text(),
                                    "cep": self.cadastrar_usuario.cep.text(),
                                    "endereco": self.cadastrar_usuario.endereco.text(),
                                    "numero": self.cadastrar_usuario.numero.text(),
                                    "bairro": self.cadastrar_usuario.bairro.text()
                                    })
            self.cadastrar_usuario.nome.setText("")
            self.cadastrar_usuario.email.setText("")
            self.cadastrar_usuario.telefone.setText("")
            self.cadastrar_usuario.cpf.setText("")
            self.cadastrar_usuario.cep.setText("")
            self.cadastrar_usuario.endereco.setText("")
            self.cadastrar_usuario.numero.setText("")
            self.cadastrar_usuario.bairro.setText("")

            self.show()
        else:
            print('erro')

              
    def show(self):

        
        data = usuario_model.getDados()
        
        if (data):
            self.cadastrar_usuario.tableWidget.setRowCount(len(data))
            self.cadastrar_usuario.tableWidget.setColumnCount(len(data[0]))

            self.cadastrar_usuario.tableWidget.setHorizontalHeaderLabels(('ID', 'NOME', 'EMAIL', 'TELEFONE', 'CPF', 'CEP', 'ENDERECO', 'NUMERO', 'BAIRRO'))
            for linha in range(len(data)):
                for coluna in range(len(data[0])):
                    self.cadastrar_usuario.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(data[linha][coluna])))
            
            return self.cadastrar_usuario.show()
        else:
            print('nao existem dados')

    def preencher_cep(self):
        dados_cep = Viacep.getCep(self.cadastrar_usuario.cep.text())
        self.cadastrar_usuario.endereco.setText(dados_cep["logradouro"])
        self.cadastrar_usuario.bairro.setText(dados_cep["bairro"])

    def voltar(self):
        self.app.quit()