# Script criado por Filipe Cavinato

from classe import Diario
from rich import inspect

def main():
    d = Diario()

    d.escrever('Primeira Mensagem')
    d.escrever('Você é uma pessoa simpática')
    d.escrever('Você gosta de Python')
    d.ler('CeV!@')
    inspect(d, private=True, methods=True)

if __name__ == '__main__':
    main()
