class Cliente:
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.__cpf = cpf
    
    def cadastrar(self) -> bool:
        self.nome = self.nome
        self.__cpf = self.__cpf
        return True