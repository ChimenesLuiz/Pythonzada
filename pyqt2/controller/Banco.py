import sqlite3

class Banco:
    def __init__(self) -> None:
        self.conn = ""
        self.cursor = ""
    
    def conectar(self):
        self.conn = sqlite3.connect('locadora.db')
        self.cursor = self.conn.cursor()