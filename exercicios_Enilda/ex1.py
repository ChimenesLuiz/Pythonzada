""" 1- O usuário deverá escolher uma opção de acordo com o último número da placa do carro e mostre uma mensagem dizendo em que dia da semana não poderá circular. 

1- 2 “Não Circular 2ª Feira” 

3 - 4 “Não Circular 3ª Feira” 

5 - 6 “Não Circular 4ª Feira” 

7- 8 “Não Circular 5ª Feira” 

9 - 0 “Não Circular 6ª Feira”  """


placa = input("Digite sua placa: ")
ultimo = placa[-1]

match ultimo:
    case "0":
        print("Nao circular na sexta feira")
    case "2":
        print("Nao circular na segunda feira")
    case "4":
        print("Nao circular na terca feira")
    case "6":
        print("Nao circular na quarta feira")
    case "8":
        print("Nao circular na quinta feira")