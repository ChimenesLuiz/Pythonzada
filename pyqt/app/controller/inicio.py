import typing
from PyQt6 import QtCore, uic, QtWidgets

#classe interna
from app.controller.usuariocontroller import UsuarioController
usuario_controller = UsuarioController()


class InicioController():


    def build(self):
        self.app = QtWidgets.QApplication([])
        self.inicio = uic.loadUi("resources/views/inicio_view.ui")
        self.inicio.show()
        self.inicio.btn_cadastrar_usuario.clicked.connect(self.ir_cadastro_usuario)

        return self.app.exec()

    def ir_cadastro_usuario(self):
        self.app.quit()
        usuario_controller.build()