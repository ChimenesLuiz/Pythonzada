import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QApplication, QStackedWidget

class Tela1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Tela 1")
        layout.addWidget(self.label)
        self.button = QPushButton("Ir para Tela 2")
        layout.addWidget(self.button)
        self.setLayout(layout)

class Tela2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Tela 2")
        layout.addWidget(self.label)
        self.button = QPushButton("Ir para Tela 1")
        layout.addWidget(self.button)
        self.setLayout(layout)

class AppController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicativo com Várias Telas")
        self.setGeometry(100, 100, 400, 300)

        # Crie um widget central com um layout de pilha para as telas
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.stacked_widget = QStackedWidget()
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.stacked_widget)

        # Crie instâncias das telas
        self.tela1 = Tela1()
        self.tela2 = Tela2()

        # Adicione as telas à pilha de widgets
        self.stacked_widget.addWidget(self.tela1)
        self.stacked_widget.addWidget(self.tela2)

        # Conecte os botões das telas aos métodos de troca de tela
        self.tela1.button.clicked.connect(self.show_screen2)
        self.tela2.button.clicked.connect(self.show_screen1)

        # Mostre a primeira tela
        self.show_screen1()

    def show_screen1(self):
        self.stacked_widget.setCurrentWidget(self.tela1)

    def show_screen2(self):
        self.stacked_widget.setCurrentWidget(self.tela2)

def main():
    app = QApplication(sys.argv)
    window = AppController()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
