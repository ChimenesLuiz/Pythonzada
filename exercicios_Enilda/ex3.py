""" 3 - O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada semestre. Os pontos são atribuídos da seguinte forma: 

•Se um cliente comprar 0 livros, ele ganhará 0 pontos. 

•Se um cliente comprar 1 livro, ele ganhará 5 pontos. 

•Se um cliente comprar 2 livros, ele ganhará 15 pontos. 

•Se um cliente comprar 3 livros, ele ganhará 30 pontos. 

•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos. 

Lista de brindes:  

De 20 à 30 pontos o cliente poderá escolher entre: Uma Ecoa OU Caneta personalizada De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira. Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank. 

 Obs: Os pontos são acumulativos, e contado a cada compra realizada pelo cliente. Ex: Se o cliente na semana 1 comprar 2 livros de uma única vez ele receberá 15 pontos, se na semana 2 ele comprar 1 único livro receberá 5 pontos totalizando 20 pontos em duas semamas. Crie um programa que leia o número de livros comprado por um usuário e exiba o número de pontos correspondentes e qual brinde ele poderá escolher. 
 """
 
def validarIntFloat(nome = str):
    while 1 == 1:
        try:
            id_produto = int(input(f"{nome}: "))
            return id_produto
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro/decimal.")
            
print("Programa fidelidade de determinada livraria")


pontos = 0

for semana in range(1, 25):
    print(f"Semana {semana}")
    while 1 == 1:
        livro = validarIntFloat("Deseja comprar quantos livros: ")
        match (livro):
            case 0:
                pontos += 0
                break
            case 1:
                pontos += 5
                break
            case 2:
                pontos += 15
                break
            case 3:
                pontos += 30
                break
            case 4:
                pontos += 60
                break

if (pontos >= 20 and pontos <= 35):
    premio = validarIntFloat("[1] - Ecoa \n[2] - Caneta personalizada \nEscolha seu premio: ")
elif (pontos >= 35 and pontos <= 60):
    premio = validarIntFloat("[1] - Luminaria de cabeceira \n[2] - Livro com valor maximo de R$30,00 \nEscolha seu premio: ")
else:
    premio = validarIntFloat("[1] - Livro A + Livro B \n[2] - Powerbank \nEscolha seu premio: ")

print("Obrigado por participar!")