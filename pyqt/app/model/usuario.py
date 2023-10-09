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

        nome = dados["nome"]
        email = dados["email"]
        telefone = dados["telefone"]
        cpf = dados["cpf"]
        cep = dados["cep"]
        endereco = dados["endereco"]
        numero = dados["numero"]
        bairro = dados["bairro"]

        consulta = "INSERT INTO usuarios (nome, email, telefone, cpf, cep, endereco, bairro, numero) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(consulta, (str(nome), str(email), str(telefone), str(cpf), str(cep), str(endereco), str(bairro), str(numero)))
        self.conn.commit()


        self.desconectar()

    
    #READ
    def getDados(self) -> tuple or list:
        self.conectar()

        consulta = "SELECT * FROM usuarios"
        self.cursor.execute(consulta)
        dados = self.cursor.fetchall()
        
        self.desconectar()
        return dados