import sqlite3
import datetime
import time
from entity.Outros import Outros

class Banheiro:
    def __init__(self, total_box = int) -> None:
        self.total_box = total_box
        self.status = 0
        self.limite_tempo = datetime.datetime.now()

        self.gambiarra = False #NAO PODE FALTAR NE, SOU EU AQUI -->> Luizao 


    def conectar(self) -> None:
        self.conn = sqlite3.connect('banheiros.db')
        self.cursor = self.conn.cursor()


    def desconectar(self) -> None:
        self.conn.close()


    def cadastrarBox(self) -> None:
        self.conectar()

        dados_fixo = (str(self.status), str(self.limite_tempo))
        parametros_insert = []
        for box in range(1, (self.total_box + 1)):
            parametros_insert.append(dados_fixo)
        self.cursor.executemany("INSERT INTO boxes(status, limite_tempo) VALUES (?, ?)", parametros_insert)


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


    def calcDatetime_Dif(self, hora_banco = str) -> None:
        hora_atual = datetime.datetime.now()
        diferenca = hora_atual - hora_banco
        return diferenca


    def converterInteiro(self, parametro = list) -> None:
        dados = parametro
        for sublista in dados:
            tempo_string = sublista[1]
            tempo_objeto = datetime.datetime.strptime(tempo_string, "%Y-%m-%d %H:%M:%S.%f")
            segundos_totais = tempo_objeto.hour * 3600 + tempo_objeto.minute * 60 + tempo_objeto.second + tempo_objeto.microsecond / 1e6

            sublista[1] = segundos_totais
        print(dados)






    def verificarTempo(self, tempo = 5):
        tempo_contador = tempo
        while 1 == 1:
            time.sleep(1)
            tempo_contador -= 1
            if (tempo_contador == 0):
                dados = self.getDatetime()
                dados = [list(t) for t in dados]

                # for sublista in dados:
                #     data_banco = datetime.datetime.strptime(sublista[1], "%Y-%m-%d %H:%M:%S.%f")
                #     diferenca = self.calcDatetime_Dif(data_banco)
                #     sublista[1] = diferenca

                dados = self.converterInteiro(dados)
                print(dados)
                break

    def getDatetime(self, id = int) -> list:
        self.conectar()

        query = "SELECT id, limite_tempo FROM boxes"
        self.cursor.execute(query)
        dados = self.cursor.fetchall()
        return dados




    def ocuparDesocupar(self, id = int) -> bool:

        if (self.verificarBox(id = id)):
            self.gambiarra = False

            self.conectar()

            query = "SELECT status FROM boxes WHERE id = ?"
            self.cursor.execute(query, (str(id),))
            verificacao_status = self.cursor.fetchone()

            if (verificacao_status[0] == 1):
                
                query = "UPDATE boxes SET status = ?, limite_tempo = ? WHERE id = ?"

                self.limite_tempo = datetime.datetime.now()
                self.cursor.execute(query, (str(0), str(self.limite_tempo), str(id)))
            else:
                query = "UPDATE boxes SET status = ?, limite_tempo = ? WHERE id = ?"

                self.limite_tempo = datetime.datetime.now()
                self.cursor.execute(query, (str(1), str(self.limite_tempo), str(id)))

            self.conn.commit()
            self.desconectar()

            return True

        else:
            self.gambiarra = True
            return False
            

    def getBox(self) -> print:
        #Outros.clearTerminal()
        print(Outros.corLilas('FBroom'))
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