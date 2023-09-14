import os
import time

class Outros:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def validarInt(nome = str):
        while 1 == 1:
            try:
                valor = int(nome)
                return valor
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
                
    @staticmethod
    def validarIntInput(nome = str):
        while 1 == 1:
            try:
                valor = int(input(f"{nome}: "))
                return valor
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
                
    @staticmethod        
    def corVermelho(texto) -> str:
        return (f'\033[1;33;41m{texto}\033[m')
    
    @staticmethod        
    def corVerde(texto) -> str:
        return (f'\033[1;32;42m{texto}\033[m')
    
    @staticmethod        
    def clearTerminal() -> None:
        # Verifica o sistema operacional
        if os.name == 'posix':
            os.system('clear')  # Para sistemas Unix-like (Linux, macOS)
        elif os.name == 'nt':
            os.system('cls')    # Para sistemas Windows

    def tempoLimite():
        segundos = 10  # Uma hora possui 3600 segundos
        
        while (segundos > 0):
            minutos, segundos = divmod(segundos, 60)
            time.sleep(1)
            segundos -= 1
        return True