# Script criado por Filipe Cavinato

from classes import Moto, Caminhao, Drone
from rich import print
from rich.table import Table

def main():
    dist = 50

    print('[blue]Sem Tabelas: [/]')
    entrega = Moto(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}')

    entrega2 = Caminhao(dist)
    print(f'Frete de {type(entrega2).__name__} em {dist}Km = {entrega2.calcular_frete()}')

    entrega3 = Drone(dist)
    print(f'Frete de {type(entrega3).__name__} em {dist}Km = {entrega3.calcular_frete()}')

    print('\n[blue]Usando Tabelas: [/]')

    tabela = Table()
    entregas = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela.add_column("Distância")
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for items in entregas:
        tabela.add_row(f"{dist} Km", f"{type(items).__name__}", f"{items.calcular_frete()}")

    print(tabela)

if __name__ == '__main__':
    main()
