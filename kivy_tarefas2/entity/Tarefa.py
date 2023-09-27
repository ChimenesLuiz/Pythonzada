from entity.Db import Database

class Tarefa:
    def __init__(self) -> None:
        pass
    
    def cadastrar(dados_p = dict) -> bool:
        db = Database('luiz')
        
        db.insert(dados = dados_p)
    
    def getDados(self) -> list:
        db = Database('luiz')
        
        dados = db.select()
        return dados
