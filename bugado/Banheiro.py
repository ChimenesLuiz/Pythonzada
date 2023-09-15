import sqlite3

class Banheiro:
    def __init__(self, total_box = int):
        self.total_box = total_box
        self.status = 0
        self.limite_tempo = 3600


    def desconectar(self):
        self.conn.commit()
        self.conn.close()

    def cadastrarBox(self):
        self.conn = sqlite3.connect('banheiros.db')
        self.cursor = self.conn.cursor()

        query = """
            INSERT INTO boxes(status, limite_tempo) VALUES (?, ?)
                """
        # for box in range(1, (self.total_box + 1)):
        self.cursor.execute(query, (str(self.status), str(self.limite_tempo)))
        self.conn.commit()

variavel = Banheiro(1)