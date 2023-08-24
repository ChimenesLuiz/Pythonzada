class Carrinho:
    def __init__(self, valor) -> None:
        self.valor = valor
    
    def inserirValor(self, valor) -> None:
        self.valor += valor
        
    def calcularPagamento(self, valor) -> float:
        troco = valor - self.valor
        return troco
    
    def getTotal(self) -> float:
        return self.valor
    
        