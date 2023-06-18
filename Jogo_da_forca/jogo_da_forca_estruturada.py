#fiz esse codigo em homenagem a minha prossora Enilda que fez o enunciado em minha homenagem.
def vermelho(entrada):
    return f'\033[31m{entrada}\033[m'

def azul(entrada):
    return f'\033[36m{entrada}\033[m'


#dicionario que representa o carinha na forca
corpo_humano = {0: 'Cabeca', 1: 'Tronco',
                2: 'Braco esquerdo', 3: 'Braco direito',
                4: 'Perna esquerda', 5: 'Direita'}
while True:
    # tratei so com numeros, deixei os caracteres especiais de lado kkkk,
    # sem usar funcao e foda :((
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
    palavra = input('Com qual palavra deseja jogar: ')
    gambiarra = True
    for ll in palavra:
        if (ll in numeros):
            print(f'{vermelho(f"Algo deu errado! Tente novamente")}')
            gambiarra = False
    if (gambiarra == False):
        continue
    else:
        break

c = 0 # definindo variavel que vai armazenar o tamanho da palavra !IMPORTANTE!
for letra in palavra:
    c += 1

lista_palavra = [' _ '] * c #declarando lista pra separar letras

#adicionando letras da palavra na lista
for a in range(0, c):
    lista_palavra[a] = palavra[a]

#!variaveis de controle!
cont_letra = 0 #Variavel que armazena quantas letras existem na palavra
agora = 0 # Variavel criada pra falar quando o jogador vence
perdeu = 0 #variavel que conta quantas vezes voce errou
lista_letra = [''] * c # lista para falar em qual posicao estao as letras que o jogador digitou
while True:
    print(f'Sua palavra: {azul(f"{lista_letra}")}')
    tentativa = input('Digite uma letra: ')
    
    if (tentativa not in lista_palavra): #caso erre
        perdeu += 1
        if (perdeu == 7):
            msg = ''
            print(f'{vermelho(f"O jogo acabou! Voce perdeu!")}')
            print(f'{azul(f"A palavra era -> {palavra}")}')
            break
        print('Voce errou!')
        
        k = 0
        while True:
            for k in corpo_humano:
                print(f'[{k}] - {corpo_humano[k]}')
            while True:
                try:
                    qual = int(input('Qual parte voce quer perder: '))
                    break
                except:
                    print(f'{vermelho(f"Algo deu errado! Tente novamente")}')
                    continue
            
            if (qual > 5):
                print(f'{vermelho(f"Escolha um numero menor ou igual a 5!")}')
                continue
            if ('cortado' in corpo_humano[qual]):
                print(f'{azul("--- - Voce nao pode escolher um membro que ja foi cortado!")}')
                continue
            else:
                break
        membro = corpo_humano[qual]
        corpo_humano[qual] = f'{vermelho(f"{membro} Ja foi cortado! xD")}'
    
    else: #caso acerte
        for d in range(0, c):
            if (tentativa == lista_palavra[d]):
                lista_letra[d] = lista_palavra[d]
                lista_palavra[d] = ''
                cont_letra += 1 
                agora += 1
        print(f'{azul(f"Existem {cont_letra} letras nesta palavra!")}')
        cont_letra = 0 
        if (agora == c):
            print(f'{azul(f"Fim de jogo, voce venceu!")}')
            break
#se vc entendeu vc e um Deus
#tengoku daimakyou e um otimo anime, vai por mim




