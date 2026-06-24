# Script criado por Filipe Cavinato

from classes import Cafe, Leite, Cha

def main():
    bebida = Leite()
    bebida.preparar()

    bebida2 = Cha()
    bebida2.preparar()

    bebida3 = Leite()
    bebida3.preparar()

if __name__ == '__main__':
    main()