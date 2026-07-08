# Script criado por Filipe Cavinato

from classe import Credencial
from rich import inspect, print

def main():
    c = Credencial()
    print(c.senha)
    c.senha = str(input('Digite a senha: '))
    print(c.senha)
    inspect(c, private=True, methods=True)

    print(c.validar('CeV'))

if __name__ == '__main__':
    main()
