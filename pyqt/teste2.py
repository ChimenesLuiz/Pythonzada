import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QApplication

class Tela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela 1")
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout(self.central_widget)
        self.label = QLabel("Tela 1")
        layout.addWidget(self.label)
        self.button = QPushButton("Ir para Tela 2")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.ir_para_tela2)

    def ir_para_tela2(self):
        self.hide()
        tela2 = Tela2()
        tela2.show()

class Tela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela 2")
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout(self.central_widget)
        self.label = QLabel("Tela 2")
        layout.addWidget(self.label)
        self.button = QPushButton("Ir para Tela 1")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.ir_para_tela1)

    def ir_para_tela1(self):
        self.hide()
        tela1 = Tela1()
        tela1.show()

def main():
    app = QApplication(sys.argv)
    tela1 = Tela1()
    tela1.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
