import typing
import sys

from PyQt6 import QtCore, uic, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication

#classe interna
from app.controller.usuariocontroller import UsuarioController



class InicioController(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Inicio")
        self.setGeometry(100, 100, 400, 300)
        uic.loadUi("resources/views/inicio_view.ui", self)
        self.btn_cadastrar_usuario.clicked.connect(self.ir_cadastrar_usuario)

        
        
    def ir_cadastrar_usuario(self):
        #self.hide()
        usuario_controller = UsuarioController()
        usuario_controller.show()
        
        
        
