from entity.Outros import Outros
import sqlite3



class Banheiro:
    def __init__(self, total_box = int) -> None:
        self.total_box = total_box
        self.status = 0
        self.limite_tempo = 3600
        
        self.__conexao = ''
        self.cursor = ''
            
    def conectar(self) -> None:
        self.__conexao = sqlite3.connect('banheiros.db')
        self.__cursor = self.__conexao.cursor()
        
    def cadastrar(self, total_box = int, status = int, limite_tempo = int) -> None:
        self.conectar()

        total_box = int
        status = int
        limite_tempo = int

        self.__cursor.execute("""
            INSERT INTO banheiros(total_box, status, limite_tempo)
            VALUES (?, ?, ?)
                            """, total_box, status, limite_tempo)
    def ocupar(self, box = int) -> None:
        self.conectar()

        total_box = int
        status = int
        limite_tempo = int
        
        self.__cursor.execute("""
            INSERT INTO banheiros(total_box, status, limite_tempo)
            VALUES (?, ?, ?)
                            """, total_box, status, limite_tempo)
        
    
    def getBox(self):
        Outros.clearTerminal()
        for c in self.box.keys():
            print('-'*30)
            print(f"{c}", end = ' ')
            print(Outros.corVermelho('OCUPADO')) if self.box[c] == 1 else print(Outros.corVerde('LIVRE'))
            print('-'*30)