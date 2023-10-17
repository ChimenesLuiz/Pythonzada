#CLASSES INTERNAS
#-----model------
from app.database.Sqlite import Sqlite
orm_sqlite = Sqlite()
#---------------------

class TaskModel:
    def __init__(self) -> None:
        pass

    def insert(self, dados = dict) -> None:
        orm_sqlite.conectar()

        consulta = "INSERT INTO tasks (task, date, completed) VALUES (:task, :date, :completed)"
        orm_sqlite.cursor.execute(consulta, dados)
        orm_sqlite.conexao.commit()

        orm_sqlite.desconectar()

    def select(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass
