class Produto:
    def __init__(self, nome, valor, id) -> None:
        self.id = id
        self.nome = nome
        self.valor = valor
    
    def cadastrar(self) -> bool:
        self.id = self.id
        self.nome = self.nome
        self.valor = self.valor
        return True
