import sqlite3
import io

from app.controllers.DirectoryController import DirectoryController

class Sqlite:
    def __init__(self) -> None:
        self.conexao = ""
        self.cursor = ""
    
    def criar(self, table = "") -> None:
        self.conectar()

        self.conexao = sqlite3.connect("todo.db")
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table}(id integer PRIMARY KEY AUTOINCREMENT, task varcahr(50) NOT NULL, date varchar(50), completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)) DEFAULT 0)''')


        self.desconectar()

    def conectar(self) -> None:
        self.conexao = sqlite3.connect("todo.db") 
        self.cursor = self.conexao.cursor()
        
    def desconectar(self) -> None:
        self.conexao.close()
        self.cursor = ""

    def importar(self, file = str) -> None:
        self.conectar()
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()

        f = io.open(file, 'r')
        sql = f.read()
        cursor.executescript(sql)

        conn.close()

    def exportar(self) -> None:
        conn = sqlite3.connect('todo.db')

        with io.open('todo_dump.sql', 'w') as f:
            for linha in conn.iterdump():
                f.write('%s\n' % linha)

        DirectoryController.rewriteDumpFile(file = 'todo_dump.sql')

        conn.close()