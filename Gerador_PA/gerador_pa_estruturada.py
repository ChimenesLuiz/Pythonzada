print('-' * 20, 'Gerador de PA', '-' * 20)
#ANA, ANA, E UM REAL A PALMA DA BANANA
lista_pas = list(); antiga = 0 #gambiarra?
while True:
    escolha = int(input('[1] - Gerar PA \n[2] - Escolher PA \n[3] - Editar PA \n[0] - Sair \nEscolha: '))
    if (escolha == 1):
        pa = list()
        #calculando PA
        p = int(input('Primeiro numero da PA: '))
        t = int(input('Total de numeros da PA: '))
        r = int(input('Razao da PA: '))
        u = 1 + p + ((t - 1) * r)
        for elemento in range(p, u, r):
            pa.append(elemento)
        #armazenando pa em lista
        lista_pas.append(pa.copy())
        pa.clear()
    elif (escolha == 2):
        c = 0
        #imprimindo todas as pas
        for pas in lista_pas:
            print(f'PA numero {c}: {pas}')
            c += 1
        escolha = int(input('Qual PA deseja usar: '))
        #vendo se oq o usuario escolheu e valido-
        if (escolha < len(lista_pas)):
            escolhida = lista_pas[escolha]
            antiga = escolhida.copy()
            numero_escolhida = escolha
            print(f'A PA escolhida foi a: {escolhida}')
        else:
            print('A PA escolhida nao existe!')
    elif (escolha == 3):
        #vendo se oq o usuario escolheu e valido
        if (len(lista_pas) > 0 and antiga != 0):
            escolha = int(input('[1] - Redefinir PA \n[2] - Excluir PA \n[0] - Voltar \nEscolha: '))
            if (escolha == 1):
                #refazendo pa, mesmo processo do comeco
                p = int(input('Primeiro numero da PA: '))
                t = int(input('Total de numeros da PA: '))
                r = int(input('Razao da PA: '))
                u = 1 + p + ((t - 1) * r)
                for elemento in range(p, u, r):
                    pa.append(elemento)
                lista_pas[numero_escolhida] = pa.copy()
                pa.clear()
                #imprimindo na tela o resultado para o usuario
                print(f'Antiga PA: {antiga} \nNova PA: {lista_pas[numero_escolhida]}')

            elif (escolha == 2):
                #deletando pa escolhida da 'lista mae de todas'
                lista_pas.remove(escolhida)
                print('A PA escolhida foi removida com sucesso!')
        else:
            print('Nao existem PAS para serem editadas, ou vc nao escolheu uma!')
    else:
        break