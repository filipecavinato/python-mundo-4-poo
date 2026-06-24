# Script criado por Filipe Cavinato

from classes import Quadrado, Circulo
from rich import print

def main():
    p1 = Quadrado(12)
    print('Quadrado:')
    print(f'Perímetro = [cian]{p1.perimetro():.1f}[/]')
    print(f'Area = [cian]{p1.area():.1f}[/]')

    p2 = Circulo(20)
    print('Circulo:')
    print(f'Perímetro = [cian]{p2.perimetro():.1f}[/]')
    print(f'Area = [cian]{p2.area():.1f}[/]')

if __name__ == '__main__':
    main()
