""" 4 - Desenvolva um sistema simulando um banco 24 horas em Python, utilizando Programação Orientada a Objetos (POO). O sistema deve permitir a criação e manipulação de contas banárias, saques e depósitos em caixas eletrônicos. Além disso, cada conta bancária terá um limite diário de saque. 
 """
from classes.Conta import Conta

def validarIntFloat(nome = str):
    while 1 == 1:
        try:
            id_produto = int(input(f"{nome}: "))
            return id_produto
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro/decimal.")

lista_objetos = []

print("Bem vindo ao banco do Luiz")
while 1 == 1:
    escolha = validarIntFloat("[1] - Cadastrar nova conta \n[2] - Consultar dados de conta pelo ID \n[3] - Depositar valor por ID \n[4] - Sacar valor por ID \n[5] - Passar o dia \n[0] - Sair \nEscolhe: ")
    
    match (escolha):
        case 0:
            break
        case 1:
            id = validarIntFloat("id: ")
            nome = input("nome: ")
            email = input("email: ")
            nome = Conta(id, nome, email, 0, 5000)
            nome.cadastrar()
            lista_objetos.append(nome)
            nome = ''
            
        case 2:
            escolha = validarIntFloat("Digite o id do usuario: ")
            for objeto in lista_objetos:
                if (escolha == objeto.id):
                    dados = objeto.getDados()
                    print(dados)

        case 3:
            escolha = validarIntFloat("Digite o id do usuario: ")
            valor = validarIntFloat("Digite o valor a ser depositado: ")
            for objeto in lista_objetos:
                if (escolha == objeto.id):
                    objeto.depositar(valor)
                    print(f"Voce depositou {valor}R$ na sua conta")
                    
        case 4:
            escolha = validarIntFloat("Digite o id do usuario: ")
            valor = validarIntFloat("Digite o valor a ser sacado: ")
            for objeto in lista_objetos:
                if (escolha == objeto.id):
                    if (objeto.sacar(valor)):
                        print(f"Voce sacou {valor}R$ da sua conta")
                    else:
                        print(f"Algo deu errado com seu saque verifique seu limite diario ou saldo")
    
        case 5:
            for objeto in lista_objetos:
                objeto.passarDia()
                print("O dia foi passado e seu limite diario foi resetado")
                    
        

            

