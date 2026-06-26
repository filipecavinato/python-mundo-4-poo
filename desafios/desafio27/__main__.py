# Script criado por Filipe Cavinato

from classes import Guerreiro, Mago
from rich import print

def main():
    p1 = Guerreiro('Kratos', 3000)
    p2 = Mago('Merlin', 3000)
    contador = 1

    while p1.vivo and p2.vivo:
        print(f'\n[bold yellow]Round {contador}:[/]')
        contador += 1
        p1.atacar(p2, 1000)
        p2.curar()
        p2.atacar(p1, 1000)
        p1.curar()

    p1.game_over(p2)

if __name__ == '__main__':
    main()
