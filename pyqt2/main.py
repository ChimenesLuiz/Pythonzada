import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__() 
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        
        
if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    
    #loading style 
    
    with open('style.qss', 'r') as style_file:
        style_str = style_file.read()
    
    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())