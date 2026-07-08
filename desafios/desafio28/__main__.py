# Script criado por Filipe Cavinato

from classe import Termostato
from rich import inspect, print

def main():
    t = Termostato()
    t.temperatura = 24
    #inspect(t, private=True, methods=True)
    print(f'A Temperatura atual é {t.ftemperatura}')

if __name__ == '__main__':
    main()
