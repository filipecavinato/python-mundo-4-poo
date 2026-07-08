# Script criado por Filipe Cavinato

from classe import Credencial
from rich import inspect, print

def main():
    c = Credencial()
    c.senha = str(input('Digite a senha: ')).strip()
    print(f'Senha = {c.senha} (Hash)')
    #inspect(c, private=True, methods=True)    # Analise da Classe usando inspect

    print(c.validar('CeV!@'))

if __name__ == '__main__':
    main()
