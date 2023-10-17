#CLASSES INTERNAS
#-----model------
from app.database.Sqlite import Sqlite
orm_sqlite = Sqlite()
#---------------------

class TaskModel:
    def __init__(self) -> None:
        pass

    def insertWithLastID(self, dados = dict) -> str or int:
        orm_sqlite.conectar()

        consulta = "INSERT INTO tasks (task, date) VALUES (:task, :date)"
        orm_sqlite.cursor.execute(consulta, dados)
        last_id = orm_sqlite.cursor.lastrowid
        orm_sqlite.conexao.commit()

        orm_sqlite.desconectar()
    
        return last_id

    def selectByID(self, id = str) -> None:
        orm_sqlite.conectar()
        consulta = "SELECT * FROM tasks WHERE id = ?"
        last_id = orm_sqlite.cursor.execute(consulta, (id,)).fetchone()

        orm_sqlite.desconectar()

        return last_id


    def select(self) -> None:
        orm_sqlite.conectar()

        consulta = "SELECT * FROM tasks"
        data = orm_sqlite.cursor.execute(consulta).fetchall()
        orm_sqlite.desconectar()
    
        return data
    


    def update(self) -> None:
        pass

    def deleteByID(self, id = str) -> None:
        orm_sqlite.conectar()

        consulta = "DELETE FROM tasks WHERE id = ?"
        orm_sqlite.cursor.execute(consulta, (id,))
        orm_sqlite.conexao.commit()

        orm_sqlite.desconectar()