class Pagamento:
    def __init__(self, pix = 0) -> None:
        self.__pix = pix
        
    def pagarPix(self, compra) -> bool:
        validacao = compra - self.__pix
        if (validacao >= 0):
            return True
        else:
            return False
        #regra de negocio pra comunicar com a API de validacao de pagamento

    
    def pagarDinheiro(self, compra, pagamento):
        troco = compra - pagamento
        if (troco < 0):
            return False
        else:
            return troco
            
        
        