import requests

class Viacep():


    @staticmethod
    #entrada bruta: 79081488
    def getCep(cep) -> bool:
        if (not cep.isdigit()):
            return False


        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'

            requisicao = requests.get(link)

            dados = requisicao.json()
            return dict(dados)
        else:
            return False
