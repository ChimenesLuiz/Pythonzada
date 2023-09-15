import sqlite3

class Banheiro:
    def __init__(self, total_box = int):
        self.total_box = total_box
        self.status = 0
        self.limite_tempo = 3600


    def desconectar(self):
        self.conn.commit()  # Salvar as alterações no banco de dados
        self.conn.close()

    def cadastrarBox(self):
        self.conn = sqlite3.connect('banheiros.db')
        self.cursor = self.conn.cursor()

        query = """
            INSERT INTO boxes(status, limite_tempo) VALUES (?, ?)
                """
        # for box in range(1, (self.total_box + 1)):
        self.cursor.execute(query, (str(self.status), str(self.limite_tempo)))


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