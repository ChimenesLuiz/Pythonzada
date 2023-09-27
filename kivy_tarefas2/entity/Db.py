import mysql.connector


def implode(separator, iterable):
    return separator.join(map(str, iterable))

class Database():
    def __init__(self, table = str) -> None:
        self.__conn = ''
        self.__cursor = ''
        self.__table = table
        
    
    def __connect(self) -> mysql.connector.Error:
        try:
            self.__conn = mysql.connector.connect(
            host="192.168.22.9",
            database = "tasks",
            user="fabrica",
            password="fabrica@2022")
            
            self.__cursor = self.__conn.cursor()
        except mysql.connector.Error as e:
            raise(f'Algo deu errado --> {e}')
    
    
    def __disconect(self) -> None:
        self.__conn.disconnect()
    
    
    def __executeQuery(self, query = str) -> list:
        self.__connect()
        try:
            self.__cursor.execute(query)
            statement = self.__cursor.fetchall()
            self.__conn.commit()
            return statement
        except mysql.connector.Error as e:
            raise(f'Algo deu errado --> {e}')
        finally:
            self.__disconect()
            
            
    def insert(self, dados = dict) -> bool:
        
        keys = []
        values = []
        for key, value in dados.items():
            keys.append(key)
            values.append(value)

        query = f"""INSERT INTO {self.__table}({implode(", ", keys)}) VALUES('{implode("', '", values)}')"""
        
        self.__executeQuery(query = query)
        return True
            
    
    def select(self, where = "", like_dados = "", order = "", limit = "", campos = "*") -> str:
        
        like = ""
        if (len(like_dados) > 0):
            where = f"WHERE " + where
            like += f"{where} LIKE {like_dados}"
        
        where = f" WHERE " + where if (len(where) > 0) else ""
        
        order = f" ORDER BY " + order if (len(order) > 0) else ""
        
        limit = f" LIMIT " + limit if (len(limit) > 0) else ""
        if (len(like) == 0):
            query = f"""SELECT {campos} FROM {self.__table} {where} {like} {order} {limit}"""
        else:
            query = f"""SELECT {campos} FROM {self.__table} {like} {order} {limit}"""
        return self.__executeQuery(query = query)
        

    def update(self, dados   = {}, where = "") -> bool:
        where = f" WHERE " + where if (len(where) > 0) else ""

        setter = ""
        for key, value in dados.items():
            setter += f"{key} = '{value}', "

        setter = setter[:-2]
        query = f"""UPDATE {self.__table} SET {setter} {where}"""

        self.__executeQuery(query = query)
        return True
    
    
    def delete(self, where = "") -> bool:
        where = f" WHERE " + where if (len(where) > 0) else ""
        
        query = f"""DELETE FROM {self.__table} {where}"""
        self.__executeQuery(query = query)
        return True    

# INSERT
# db = Database('luiz')
# dados = {"nome": "tarefa", "descricao": "descricao tarefa", "data_tarefa": "2023-09-26", "estado_tarefa": "F"}
# db.insert(dados = dados)
    
# SELECT
# db = Database('luiz')
# dados = db.select()
# print(dados)

# UPDATE
# db = Database('luiz')
# dados = {"descricao": "AAAAAAAAAAAAAAAAA", "estado_tarefa": "N"}
# db.update(dados = dados, where = "id = 1")

# DELETE
# db = Database('luiz')
# db.delete(where = "id = 1")


    