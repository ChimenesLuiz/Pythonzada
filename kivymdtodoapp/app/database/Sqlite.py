import sqlite3

class Sqlite:
    def __init__(self) -> None:
        self.conexao = ""
        self.cursor = ""
    
    def conectar(self) -> None:
        self.conexao = sqlite3.connect("todo.db") 
        self.cursor = self.conexao.cursor()
        
    def desconectar(self) -> None:
        self.conexao.close()
        self.cursor = ""
