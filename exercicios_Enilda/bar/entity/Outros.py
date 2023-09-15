import os

class Outros:
    
    @staticmethod
    def validarInt(nome = str) -> int or print:
        while 1 == 1:
            try:
                valor = int(nome)
                return valor
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
                
    @staticmethod
    def validarIntInput(nome = str) -> str or print:
        while 1 == 1:
            try:
                valor = int(input(f"{nome}: "))
                return valor
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
                
    @staticmethod        
    def corVermelho(texto) -> str:
        return (f'\033[1;31;41m{texto}\033[m') #bold, vermelho, vermelho
    
    @staticmethod        
    def corVerde(texto) -> str:
        return (f'\033[1;32;42m{texto}\033[m') #bold, verde, verde
    
    @staticmethod        
    def corLilas(texto) -> str:
        return (f'\033[1;35;40m{texto}\033[m') #bold, lilas, preto
    
    @staticmethod        
    def corAzul(texto) -> str:
        return (f'\033[1;36;46m{texto}\033[m') #bold, azul, azul

    @staticmethod        
    def corAmarelo(texto) -> str:
        return (f'\033[1;33;43m{texto}\033[m') #bold, amarelo, amarelo
    
    @staticmethod        
    def clearTerminal() -> None:
        # Verifica o sistema operacional
        if os.name == 'posix':
            os.system('clear')  # Para sistemas Unix-like (Linux, macOS)
        elif os.name == 'nt':
            os.system('cls')    # Para sistemas Windows
