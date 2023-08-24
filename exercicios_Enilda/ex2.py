""" 2- Menu com opções de um cardápio de restaurante para uma pessoa (Coloque no mínimo 5 opções. Ex: Bife acebolado R$15,00; Lasanha R$25,00). A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário, “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso contrário, mostrar o valor final (somente o valor do prato).  """

def validarIntFloat(nome = str):
    while 1 == 1:
        try:
            id_produto = int(input(f"{nome}: "))
            return id_produto
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro/decimal.")

total = 0
while 1 == 1:
    while 1==1:
        try:
            escolha = validarIntFloat("[1] - Bife acebolado \n[2] - Lasanha \n[3] - Bife sem cebola \n[4] - Picole de leite condenado \n[5] - Suquinho de couve \n[0] - Sair \nEscolha sua opcao: ")
            break
        except:
            print("Algo deu errado")
            continue
    match escolha:
        case 0:
            break
        case 1:
            while 1==1:
                try:
                    escolha_2 = validarIntFloat("[1] - Sim \n[2] - Nao \nAceita pagar a gorjeta de 10%, do garcom sobre o valor do prato? ")
                    break
                except:
                    print("Algo deu errado")
                    continue

            if (escolha_2 == 1):
                total += 60 + (60 * 0.1)
            else:
                total += 60
        case 2:
            while 1==1:
                try:
                    escolha_2 = validarIntFloat("[1] - Sim \n[2] - Nao \nAceita pagar a gorjeta de 10%, do garcom sobre o valor do prato? ")
                    break
                except:
                    print("Algo deu errado")
                    continue                    
            if (escolha_2 == 1):
                total += 100 + (100 * 0.1)
            else:
                total += 100
        case 3:
            while 1==1:
                try:
                    escolha_2 = validarIntFloat("[1] - Sim \n[2] - Nao \nAceita pagar a gorjeta de 10%, do garcom sobre o valor do prato? ")
                    break
                except:
                    print("Algo deu errado")
                    continue
                    
            if (escolha_2 == 1):
                total += 50 + (50 * 0.1)
            else:
                total += 50
        case 4:
            while 1==1:
                try:
                    escolha_2 = validarIntFloat("[1] - Sim \n[2] - Nao \nAceita pagar a gorjeta de 10%, do garcom sobre o valor do prato? ")
                    break
                except:
                    print("Algo deu errado")
                    continue
            if (escolha_2 == 1):
                total += 20 + (20 * 0.1)
            else:
                total += 20
        case 5:
            while 1==1:
                try:
                    escolha_2 = validarIntFloat("[1] - Sim \n[2] - Nao \nAceita pagar a gorjeta de 10%, do garcom sobre o valor do prato? ")
                    break
                except:
                    print("Algo deu errado")
                    continue                
            if (escolha_2 == 1):
                total += 30 + (30 * 0.1)
            else:
                total += 30
                
print(f"O total da compra foi: {total}")