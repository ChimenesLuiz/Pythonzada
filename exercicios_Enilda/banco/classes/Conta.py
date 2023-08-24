class Conta:
    def __init__(self, id, nome, email, saldo, limite) -> None:
        self.id = id
        self.nome = nome
        self.email = email
        self.saldo = saldo
        self.limite = limite

    def cadastrar(self) -> bool:
        try:
            self.id = self.id
            self.nome = self.nome
            self.email = self.email
            self.saldo = self.saldo
            self.limite = self.limite
            return True
        except:
            return False

    def depositar(self, saldo) -> bool:
        self.saldo += saldo
        return True

        
    def sacar(self, saque) -> bool:
        if ((self.limite - saque) < 0 or saque > self.saldo):
            return False  
        else:      
            self.saldo -= saque
            self.limite -= saque
            return True
    
    
    def getDados(self) -> str:
        lista = {"id": self.id, "nome": self.nome, "email": self.email, "saldo": self.saldo, "limite": self.limite}
        return lista
    
    def passarDia(self):
        self.limite = 5000
        