""" 6 – Crie um sistema de controle de estoque e vendas em python utilizando POO, no qual deverá cadastrar o produto, o cliente e a forma de pagamento, o cliente poderá escolher mais de um produto e quando encerrar as escolhas dos produtos deverá aparecer o valor total a pagar, posteriormente deverá aparecer as opções de pagamento: Em dinheiro ou pix, se for o pix deverá informar o número da chave e se for em dinheiro deverá informar o troco e assim finalizar o sistema.  """
from classes.Produto import Produto
from classes.Cliente import Cliente
from classes.Pagamento import Pagamento
   
def validar_cpf():
    cpf = input("Digite seu CPF: ")
    # Removendo caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificando se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calculando os dígitos verificadores
    cpf_list = list(map(int, cpf))
    soma1 = sum([cpf_list[i] * (10 - i) for i in range(9)])
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0

    soma2 = sum([cpf_list[i] * (11 - i) for i in range(10)])
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verificando os dígitos verificadores
    if digito1 == cpf_list[9] and digito2 == cpf_list[10]:
        return cpf
    else:
        return False
            
def validarIntFloat(nome = str):
    while 1 == 1:
        try:
            id_produto = int(input(f"{nome}: "))
            return id_produto
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro/decimal.")

lista_produto = []
lista_cliente = []
sacola = {}
total_compra = 0
contador = 0
gambiarra = True

print("Mercadinho do LUIZ")

while 1 == 1:
    contador = 0
    escolha = validarIntFloat("[1] - Cadastrar produto \n[2] - Cadastrar cliente \n[3] - Cadastrar compra \n[0] - Sair \nEscolha: ")
    match (escolha):
        case 0:
            break
        case 1:
            id = validarIntFloat("Id do Produto")
            nome = input("Nome do produto: ")
            valor = validarIntFloat("Valor do produto")
            produto = Produto(nome = nome, valor = valor, id = id)
            if(produto.cadastrar()):
                print("Produto cadastrado com sucesso")
                lista_produto.append(produto)
            else:
                print("Algo deu errado ao cadastrar seu produto")
        case 2:
            nome = input("Nome: ")
            while 1 == 1:
                cpf = validar_cpf()
                if (cpf):
                    break
                else:
                    print("CPF INVALIDO")
                    continue
                    
            cliente = Cliente(nome = nome, cpf = cpf)
            if (cliente.cadastrar()):
                print("Cliente cadastrado com sucesso")
                lista_cliente.append(cliente)
                gambiarra = False
            else:
                print("Algo deu errado ao cadastrar seu cliente")
        
        case 3:
            if (gambiarra):
                print("Voce precisa cadastrar um cliente")
                continue
            while 1 == 1:
                if (contador == 0 ):
                    for nome, valor in sacola.items():
                        contador += 1
                        print(f"{contador}: {nome} ---------- {valor} ")
                    print(f"Total da compra: {total_compra}")
                else:
                    print("SACOLA VAZIA")
                    
                if (len(lista_produto) > 0):
                    escolha_2 = validarIntFloat("[1] - Adicionar novo produto na compra \n[2] - Finalizar compra\nEscolha: ")
                    match (escolha_2):
                        case 1:
                                id = validarIntFloat("Digite o id do produto: ")
                                for produto in lista_produto:
                                    if (produto.id == id):
                                        sacola.update({produto.nome: produto.valor})
                                        total_compra += produto.valor
                                        
                        case 2:
                            escolha_3 = validarIntFloat("[1] - PIX \n[2] - DINHEIRO \nEscolha: ")
                            match (escolha_3):
                                case 1:
                                    valor = validarIntFloat("Valor: ")
                                    pagamento = Pagamento(valor)
                                    if (pagamento.pagarPix(total_compra)):
                                        print("Pagamento realizado com sucesso")
                                        sacola.clear()
                                        total_compra = 0
                                        break
                                    else:
                                        print("Algo deu errado com seu pagamento")
                                        
                                
                                case 2:
                                    valor = validarIntFloat("Valor: ")
                                    pagamento = Pagamento()
                                    if (pagamento.pagarDinheiro(compra = total_compra, valor = valor)):
                                        print(f"Pagamento realizado com sucesso, seu troco: {total_compra - valor}")
                                        sacola.clear()
                                        total_compra = 0
                                        break
                                    else:
                                        print("Algo deu errado com seu pagamento")
                            
                else:
                    print("Voce nao tem produtos cadastrados ainda")
                    break
            
                        
                        
                            
            