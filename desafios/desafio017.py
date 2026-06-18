# Script criado por Filipe Cavinato

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome = None, preco = 0.0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        painel = Panel(f'{self.nome:^30}\n{'':.^30}\n{'R$':.>12}{self.preco:.<18.2f}', title='Produto',width=34 )
        print(painel)

p1 = Produto('Iphone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000.00)
p1.etiqueta()
p2.etiqueta()

print('------ Fim do Programa ------')
