import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from resources.sidebar.sidebar_ui import Ui_MainWindow
import resources.sidebar.resource_rc as resource_rc


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__() 
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        
    @staticmethod
    def build():
        app = QApplication(sys.argv)

        style_file = QFile("resources/sidebar/style.qss")
        style_file.open(QFile.ReadOnly | QFile.Text)
        style_stream = QTextStream(style_file)
        app.setStyleSheet(style_stream.readAll())
        
        window = MainWindow()
        window.show()
        return sys.exit(app.exec())
      
    #search
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        search_text = self.ui.search_input.text().strip()
        if (search_text):
            self.ui.label_7.setText(search_text)
            
    #user
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)    
        
    #change qpushbutton checkable status when stackedwidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) + self.ui.full_menu_widget.findChildren(QPushButton) 
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
                
        ## functions for changing menu page
    
    #switching screens
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_usuario_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_usuario_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_veiculo_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_veiculo_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

        
        

if (__name__ == '__main__'):
    MainWindow.build()