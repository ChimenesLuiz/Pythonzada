from app.controller.iniciocontroller import InicioController
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    janela = InicioController()
    janela.show()
    sys.exit(app.exec())  