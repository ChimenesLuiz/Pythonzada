import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from resources.front_end_ui import Ui_MainWindow
import resources.sidebar.resource_rc as resource_rc

#interna
from controller.Usuario import Usuario
from controller.Veiculo import Veiculo
from controller.api.viacep import Viacep
from controller.Relacao import Relacao


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__() 
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        #trocas de tela
        #cadastrar troca de tela
        self.ui.btn_cadastrar_usuario_redirect.clicked.connect(self.on_btn_cadastrar_usuario_redirect_toggled)

        self.ui.btn_cadastrar_veiculo_redirect.clicked.connect(self.on_btn_cadastrar_veiculo_redirect_toggled)

        self.ui.btn_locar_relacao_redirect.clicked.connect(self.on_btn_locar_relacao_redirect_toggled)
        #voltar troca de tela
        self.ui.btn_voltar_tela_editar_usuario_redirect.clicked.connect(self.on_usuario_btn_2_toggled)
        self.ui.btn_voltar_tela_excluir_usuario_redirect.clicked.connect(self.on_usuario_btn_2_toggled)

        self.ui.btn_voltar_tela_editar_veiculo_redirect.clicked.connect(self.on_veiculo_btn_2_toggled)
        self.ui.btn_voltar_tela_excluir_veiculo_redirect.clicked.connect(self.on_veiculo_btn_2_toggled)

        self.ui.btn_voltar_tela_editar_relacao.clicked.connect(self.on_home_btn_2_toggled)
        self.ui.btn_voltar_tela_excluir_relacao.clicked.connect(self.on_home_btn_2_toggled)
        #editar troca de tela
        self.ui.btn_editar_usuario_redirect.clicked.connect(self.on_btn_editar_usuario_redirect_toggled)
        self.ui.btn_editar_tela_editar_usuario_redirect.clicked.connect(self.editar_usuario)

        self.ui.btn_editar_veiculo_redirect.clicked.connect(self.on_btn_editar_veiculo_redirect_toggled)
        self.ui.btn_editar_tela_editar_veiculo_redirect.clicked.connect(self.editar_veiculo)

        self.ui.btn_editar_relacao_redirect.clicked.connect(self.on_btn_editar_relacao_redirect_toggled)
        #exluir troca de tela
        self.ui.btn_excluir_usuario_redirect.clicked.connect(self.on_btn_excluir_usuario_redirect_toggled)

        self.ui.btn_excluir_veiculo_redirect.clicked.connect(self.on_btn_excluir_veiculo_redirect_toggled)

        self.ui.btn_excluir_relacao_redirect.clicked.connect(self.on_btn_excluir_relacao_redirect_toggled)
        ############################################################################################


        #create
        self.ui.btn_cadastrar_usuario.clicked.connect(self.post_usuario)

        self.ui.btn_cadastrar_veiculo.clicked.connect(self.post_veiculo)

        self.ui.btn_confirmar_tela_locar_carro.clicked.connect(self.post_relacao)

        #read
        self.show_dados_usuarios()
        self.show_dados_veiculos()
        self.show_dados_relacoes()

        #update

        #delete
        self.ui.btn_excluir_tela_excluir_usuario_redirect.clicked.connect(self.excluir_usuario)

        self.ui.btn_excluir_tela_excluir_veiculo_redirect.clicked.connect(self.excluir_veiculo)
        #others
        self.ui.btn_buscar_cep.clicked.connect(self.buscar_cep)
        self.ui.btn_limpar_cadastro_usuario.clicked.connect(self.limpar_cadastro_usuario)

        self.ui.btn_limpar_dados_veiculo.clicked.connect(self.limpar_cadastro_veiculo)

        #others others
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
    #1 veiculos tabela
    #2 usuarios tabela
    #3 cadastro de usuarios
    #4 locar/vender carro
    #6 excluir id usuarios
    #8 excluir id usuario
    #9 editar id usuario
    #10 editar id veiculo
    #11 excluir id veiculo
    #12 cadastro de veiculo

    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_usuario_btn_2_toggled(self):
        self.show_dados_usuarios()
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_veiculo_btn_2_toggled(self):
        self.show_dados_veiculos()
        self.ui.stackedWidget.setCurrentIndex(1)

    #USUARIO
    def on_btn_cadastrar_usuario_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_btn_excluir_usuario_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)
    
    def on_btn_editar_usuario_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    #VEICULO
    def on_btn_cadastrar_veiculo_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def on_btn_editar_veiculo_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def on_btn_excluir_veiculo_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    #RELACAO
    def on_btn_locar_relacao_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    
    def on_btn_editar_relacao_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_btn_excluir_relacao_redirect_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    
    #end switching screens

    #Usuario logica
    def post_usuario(self):
        dados = Usuario.getDadosByCPF(cpf = str(self.ui.input_cpf.text()))
        if (dados):
            Usuario.update(dados[0], dados_update = {"nome": self.ui.input_nome_completo.text(),
                                                    "email": self.ui.input_email.text(),
                                                    "telefone": self.ui.input_telefone.text(),
                                                    "cpf": self.ui.input_cpf.text(),
                                                    "cep": self.ui.input_cep.text(),
                                                    "bairro": self.ui.input_bairro.text(),
                                                    "rua": self.ui.input_rua.text(),
                                                    "numero": self.ui.input_numero.text()
                                                    })
            self.limpar_cadastro_usuario()
            self.on_usuario_btn_2_toggled()
        else:
            dados = {"nome": self.ui.input_nome_completo.text(),
                    "email": self.ui.input_email.text(),
                    "telefone": self.ui.input_telefone.text(),
                    "cpf": self.ui.input_cpf.text(),
                    "cep": self.ui.input_cep.text(),
                    "bairro": self.ui.input_bairro.text(),
                    "rua": self.ui.input_rua.text(),
                    "numero": self.ui.input_numero.text(),
                    }
            Usuario.cadastrar(dados = dados)
            self.limpar_cadastro_usuario()
        self.ui.input_id_tela_editar_usuario.setText("")

    def buscar_cep(self):
        
        dados = Viacep.getCep(cep = str(self.ui.input_cep.text()))
        if (dados):
            self.ui.input_bairro.setText(dados["bairro"]) 
            self.ui.input_rua.setText(dados["logradouro"])
        else:
            print('saporra nao existe')
        
    def limpar_cadastro_usuario(self):
        self.ui.input_nome_completo.setText("")
        self.ui.input_email.setText("")
        self.ui.input_telefone.setText("")
        self.ui.input_cpf.setText("")
        self.ui.input_cep.setText("")
        self.ui.input_bairro.setText("")
        self.ui.input_rua.setText("")
        self.ui.input_numero.setText("")

    def show_dados_usuarios(self):
        dados = Usuario.getDados()
        if (dados):
            self.ui.tabela_usuarios.setRowCount(len(dados))
            self.ui.tabela_usuarios.setColumnCount(len(dados[0]))

            self.ui.tabela_usuarios.setHorizontalHeaderLabels(('ID', 'NOME COMPLETO', 'EMAIL', 'TELEFONE', 'CPF', 'CEP', 'BAIRRO', 'RUA', 'NUMERO'))
            for linha in range(len(dados)):
                for coluna in range(len(dados[0])):
                    self.ui.tabela_usuarios.setItem(linha, coluna, QTableWidgetItem(str(dados[linha][coluna])))
        else:
            self.ui.tabela_usuarios.setRowCount(0)
            self.ui.tabela_usuarios.setColumnCount(0)
            
    def excluir_usuario(self):
        if (Usuario.deleteById(str(self.ui.input_id_tela_excluir_usuario.text()))):
            self.on_usuario_btn_2_toggled()
            self.ui.input_id_tela_excluir_usuario.setText("")
        else:
            print("id nao existe")
        self.ui.input_id_tela_excluir_usuario.setText("")

    def editar_usuario(self):
        dados = Usuario.getDadosById(id = str(self.ui.input_id_tela_editar_usuario.text()))
        self.on_btn_cadastrar_usuario_redirect_toggled()
        self.ui.input_nome_completo.setText(str(dados[1]))
        self.ui.input_email.setText(str(dados[2]))
        self.ui.input_telefone.setText(str(dados[3]))
        self.ui.input_cpf.setText(str(dados[4]))
        self.ui.input_cep.setText(str(dados[5]))
        self.ui.input_bairro.setText(str(dados[6]))
        self.ui.input_rua.setText(str(dados[7]))
        self.ui.input_numero.setText(str(dados[8]))
    #Veiculo logica
    def post_veiculo(self):
        dados = Veiculo.getDadosByChassi(chassi = str(self.ui.input_chassi_veiculo.text()))
        if (dados):
            Veiculo.update(dados[0], dados_update =  {"ano": self.ui.input_ano_veiculo.text(),
                                                    "km": self.ui.input_km_veiculo.text(),
                                                    "cambio": self.ui.input_cambio_veiculo.text(),
                                                    "carroceria": self.ui.input_carroceria_veiculo.text(),
                                                    "combustivel": self.ui.input_combustivel_veiculo.text(),
                                                    "placa": self.ui.input_placa_veiculo.text(),
                                                    "cor": self.ui.input_cor_veiculo.text(),
                                                    "chassi": self.ui.input_chassi_veiculo.text()
                                                    })
            self.limpar_cadastro_veiculo()
            self.on_veiculo_btn_2_toggled()
        else:
            dados = {"ano": self.ui.input_ano_veiculo.text(),
                    "km": self.ui.input_km_veiculo.text(),
                    "cambio": self.ui.input_cambio_veiculo.text(),
                    "carroceria": self.ui.input_carroceria_veiculo.text(),
                    "combustivel": self.ui.input_combustivel_veiculo.text(),
                    "placa": self.ui.input_placa_veiculo.text(),
                    "cor": self.ui.input_cor_veiculo.text(),
                    "chassi": self.ui.input_chassi_veiculo.text(),
                    }
            Veiculo.cadastrar(dados = dados)
            self.limpar_cadastro_veiculo()
        self.ui.input_id_tela_editar_veiculo.setText("")

    def limpar_cadastro_veiculo(self):
        self.ui.input_ano_veiculo.setText("")
        self.ui.input_km_veiculo.setText("")
        self.ui.input_cambio_veiculo.setText("")
        self.ui.input_carroceria_veiculo.setText("")
        self.ui.input_combustivel_veiculo.setText("")
        self.ui.input_placa_veiculo.setText("")
        self.ui.input_cor_veiculo.setText("")
        self.ui.input_chassi_veiculo.setText("")

    def show_dados_veiculos(self):
        dados = Veiculo.getDados()
        if (dados):
            self.ui.tabela_veiculos.setRowCount(len(dados))
            self.ui.tabela_veiculos.setColumnCount(len(dados[0]))

            self.ui.tabela_veiculos.setHorizontalHeaderLabels(('ID', 'ANO', 'KM', 'CAMBIO', 'CARROCERIA', 'COMBUSTIVEL', 'PLACA', 'COR', 'CHASSI'))
            for linha in range(len(dados)):
                for coluna in range(len(dados[0])):
                    self.ui.tabela_veiculos.setItem(linha, coluna, QTableWidgetItem(str(dados[linha][coluna])))
        else:
            self.ui.tabela_veiculos.setRowCount(0)
            self.ui.tabela_veiculos.setColumnCount(0)

    def excluir_veiculo(self):
        if (Veiculo.deleteById(str(self.ui.input_id_tela_excluir_veiculo.text()))):
            self.on_veiculo_btn_2_toggled()
        else:
            print("id nao existe")
        self.ui.input_id_tela_excluir_veiculo.setText("")

    def editar_veiculo(self):
        dados = Veiculo.getDadosById(id = str(self.ui.input_id_tela_editar_veiculo.text()))
        self.on_btn_cadastrar_veiculo_redirect_toggled()
        self.ui.input_ano_veiculo.setText(str(dados[1]))
        self.ui.input_km_veiculo.setText(str(dados[2]))
        self.ui.input_cambio_veiculo.setText(str(dados[3]))
        self.ui.input_carroceria_veiculo.setText(str(dados[4]))
        self.ui.input_combustivel_veiculo.setText(str(dados[5]))
        self.ui.input_placa_veiculo.setText(str(dados[6]))
        self.ui.input_cor_veiculo.setText(str(dados[7]))
        self.ui.input_chassi_veiculo.setText(str(dados[8]))

    #Relacao logica
    def post_relacao(self):
        #dados = Veiculo.getDadosByChassi(chassi = str(self.ui.input_chassi_veiculo.text()))
        if (1 != 1):
            Veiculo.update(dados[0], dados_update =  {"ano": self.ui.input_ano_veiculo.text(),
                                                    "km": self.ui.input_km_veiculo.text(),
                                                    "cambio": self.ui.input_cambio_veiculo.text(),
                                                    "carroceria": self.ui.input_carroceria_veiculo.text(),
                                                    "combustivel": self.ui.input_combustivel_veiculo.text(),
                                                    "placa": self.ui.input_placa_veiculo.text(),
                                                    "cor": self.ui.input_cor_veiculo.text(),
                                                    "chassi": self.ui.input_chassi_veiculo.text()
                                                    })
            self.limpar_cadastro_veiculo()
            self.on_veiculo_btn_2_toggled()
        else:
            dados = {"id_usuario": self.ui.input_cpf_cliente_tela_locar_carro.text(),
                    "id_veiculo": self.ui.input_placa_veiculo_tela_locar_carro.text(),
                    "data_limite": self.ui.input_data_tela_locar_carro.text(),
                    "preco": self.ui.input_total_tela_locar_carro.text(),
                    "tipo": self.ui.input_tipo_tela_locar_carro.text()
                    }
            Relacao.cadastrar(dados = dados)
            self.limpar_cadastro_relacao()
        self.ui.input_id_tela_editar_relacao.setText("")
        self.show_dados_relacoes()

    def limpar_cadastro_relacao(self):
        self.ui.input_cpf_cliente_tela_locar_carro.setText("")
        self.ui.input_placa_veiculo_tela_locar_carro.setText("")
        self.ui.input_total_tela_locar_carro.setText("")
        self.ui.input_tipo_tela_locar_carro.setText("")

    def show_dados_relacoes(self):
        Relacao.getDados()
        dados = Relacao.getDados()
        print(dados)
        if (dados):
            self.ui.tabela_relacoes.setRowCount(len(dados))
            self.ui.tabela_relacoes.setColumnCount(len(dados[0]))

            self.ui.tabela_relacoes.setHorizontalHeaderLabels(('ID', 'NOME COMPLETO', 'EMAIL', 'TELEFONE', 'CPF', 'CEP', 'BAIRRO', 'RUA', 'NUMERO'))
            for linha in range(len(dados)):
                for coluna in range(len(dados[0])):
                    self.ui.tabela_relacoes.setItem(linha, coluna, QTableWidgetItem(str(dados[linha][coluna])))
        else:
            self.ui.tabela_relacoes.setRowCount(0)
            self.ui.tabela_relacoes.setColumnCount(0)

if (__name__ == '__main__'):
    MainWindow.build()