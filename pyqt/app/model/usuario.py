import sqlite3

class Usuario:
    def __init__(self) -> None:
        self.conn = ""


    def conectar(self) -> None:
        self.conn = sqlite3.connect("larissa.db")
        self.cursor = self.conn.cursor()
    
    
    def desconectar(self) -> None:
        self.conn.close()
        self.cursor = ""

    #CREATE
    def cadastrar(self, dados = {}) -> None:
        self.conectar()

        matricula = dados["matricula"]
        nome = dados["nome"]
        email = dados["email"]
        telefone = dados["telefone"]

        consulta = "INSERT INTO usuarios (matricula, nome, email, telefone) VALUES (?, ?, ?, ?)"
        self.cursor.execute(consulta, (str(matricula), str(nome), str(email), str(telefone)))
        self.conn.commit()


        self.desconectar()

    
    #READ
    def getDados(self) -> tuple or list:
        self.conectar()

        consulta = "SELECT * FROM usuarios"
        self.cursor.execute(consulta)
        dados = self.cursor.fetchall()
        return dados


        self.desconectar()