# Script criado por Filipe Cavinato

from classe import Termostato
from rich import inspect, print

def main():
    t = Termostato()
    try:
        t.temperatura = 18
    except ValueError as erro:
        print(f'[red] ERRO: {erro}[/]')

    #inspect(t, private=True, methods=True)   # Analise de Classe usando inspect
    print(f'A Temperatura atual é [blue]{t.ftemperatura}[/]')

if __name__ == '__main__':
    main()
