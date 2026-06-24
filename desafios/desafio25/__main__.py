# Script criado por Filipe Cavinato

from classes import Moto, Caminhao, Drone
from rich import print

def main():
    dist = 50
    entrega = Moto(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}')

    entrega2 = Caminhao(dist)
    print(f'Frete de {type(entrega2).__name__} em {dist}Km = {entrega2.calcular_frete()}')

    entrega3 = Drone(dist)
    print(f'Frete de {type(entrega3).__name__} em {dist}Km = {entrega3.calcular_frete()}')


if __name__ == '__main__':
    main()