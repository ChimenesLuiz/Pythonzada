""" 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando Programação Orientada a Objetos (POO). O sistema deve permitir a realização de compras, cálculo de total e troco. 
 """
from classes.Carrinho import Carrinho
carrinho = Carrinho(valor = 0)

def validarIntFloat(nome = str):
    while 1 == 1:
        try:
            id_produto = int(input(f"{nome}: "))
            return id_produto
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro/decimal.")

while 1 == 1:
    print(f"TOTAL DA COMPRA: {carrinho.getTotal()}")
    print("-" * 50)
    escolha = validarIntFloat("[1] - Ler codigo de barras/Inserir Valor \n[2] - Receber pagamento \n[3] - Limpar carrinho \n[0] - Sair \nEscolha: ")
    match (escolha):
        case 0:
            break
        case 1:
            valor = validarIntFloat("Inserir valor do produto: ")
            carrinho.inserirValor(valor = valor)
            
        case 2:
            valor = validarIntFloat("Insira o valor recebido: ")
            troco = carrinho.calcularPagamento(valor = valor)
            if (troco < 0):
                print("VALOR INSUFICIENTE PARA FINALIZAR A COMPRA")
                print("*" * 50)
            else:
                print("COMPRA FINALIZADA")
                carrinho = Carrinho(valor = 0)
        case 3:
            carrinho = Carrinho(valor = 0)
        
            