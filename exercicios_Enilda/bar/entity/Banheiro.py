import sqlite3
from entity.Outros import Outros

class Banheiro:
    def __init__(self, total_box = int) -> None:
        self.total_box = total_box
        self.status = 0

        self.gambiarra = False #NAO PODE FALTAR NE, SOU EU AQUI -->> Luizao 


    def conectar(self) -> None:
        self.conn = sqlite3.connect('banheiros.db')
        self.cursor = self.conn.cursor()


    def desconectar(self) -> None:
        self.conn.close()


    def cadastrarBox(self) -> None:
        self.conectar()

        dados_fixo = (str(self.status))
        parametros_insert = []
        for box in range(1, (self.total_box + 1)):
            parametros_insert.append(dados_fixo)
        self.cursor.executemany("INSERT INTO boxes(status) VALUES (?)", parametros_insert)

        self.conn.commit()
        self.desconectar()


    def verificarBox(self, id = int) -> bool:
        self.conectar()

        query = "SELECT COUNT(*) FROM boxes WHERE id = ?"
        self.cursor.execute(query, (str(id),))
        validacao_id = self.cursor.fetchone()
        self.desconectar()

        if (validacao_id[0] > 0):
            return True
        else:
            return False


    def ocuparDesocupar(self, id = int) -> bool:

        if (self.verificarBox(id = id)):
            self.gambiarra = False

            self.conectar()

            query = "SELECT status FROM boxes WHERE id = ?"
            self.cursor.execute(query, (str(id),))
            verificacao_status = self.cursor.fetchone()

            if (verificacao_status[0] == 1):
                
                query = "UPDATE boxes SET status = ? WHERE id = ?"

                self.cursor.execute(query, (str(0), str(id)))
            else:
                query = "UPDATE boxes SET status = ? WHERE id = ?"

                self.cursor.execute(query, (str(1), str(id)))

            self.conn.commit()
            self.desconectar()

            return True

        else:
            self.gambiarra = True
            return False
            

    def getBox(self) -> print:
        Outros.clearTerminal()
        logo = ('-'*10) + ' FBroom ' + ('-'*10)
        print(Outros.corLilas(logo))
        if (self.gambiarra):
            print(Outros.corVermelho('ALGO DEU ERRADO!!'))

        self.conectar()

        query = "SELECT * FROM boxes" 
        self.cursor.execute(query) 
        dados = self.cursor.fetchall()

        for c in dados:
            id = c[0]
            status = c[1]

            print('-'*30)
            print(f"{id}", end = ' ')
            print(Outros.corVermelho('OCUPADO')) if status == 1 else print(Outros.corVerde('LIVRE'))
            print('-'*30)