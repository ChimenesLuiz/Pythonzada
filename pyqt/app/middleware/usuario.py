from re import match

#classe interna
from app.apis.viacep import Viacep

class UsuarioMiddleware:

    @staticmethod
    def verificaEmail(email = str) -> bool:
        padrao_email = r'^[\w\.-]+@[\w\.-]+$'

        if match(padrao_email, email):
            return True
        else:
            return False
        

    @staticmethod
    #entrada bruta: 67993449090 ou 6793449090
    def verificaTelefone(numero = str) -> bool:
        if (not numero.isdigit()):
            return False

        padrao_sem_9 = r'^(\d{11}|\d{10})$'
        padrao_com_9 = r'^\d{11}$'

        if (match(padrao_com_9, numero) or match(padrao_sem_9, numero)):
            return True
        else:
            return False
    

    @staticmethod
    #entrada bruta: 08243464655
    def verificaCpf(cpf = str):
        if (len(cpf) != 11 or not cpf.isdigit()):
            return False

        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        numeros = [int(digito) for digito in cpf if digito.isdigit()]
        
        formatacao = False
        quant_digitos = False
        validacao1 = False
        validacao2 = False

        if match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            formatacao = True

        if len(numeros) == 11:
            quant_digitos = True
        
            soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
            digito_esperado = (soma_produtos * 10 % 11) % 10
            if numeros[9] == digito_esperado:
                validacao1 = True

            soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
            digito_esperado1 = (soma_produtos1 *10 % 11) % 10
            if numeros[10] == digito_esperado1:
                validacao2 = True

            if quant_digitos == True and formatacao == True and validacao1 == True and validacao2 == True:
                return True
            else:
                return False

        else:
            return False


