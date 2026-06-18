# Script criado por Filipe Cavinato

from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self):
        self.ligado = False
        self.vol = 0
        self.canal = 1
        self.painel = Panel('teste', title='TV', width=44)
        print(self.painel)

    def liga_desliga(self, comando):
        if not self.ligado and comando == '@':
            self.ligado = True
        elif self.ligado and comando == '@':
            self.ligado = False
        print(self.painel)

    def volume(self, aumentar_vol):
        self.vol += aumentar_vol
        return self.vol

c1 = ControleRemoto()
c1.liga_desliga('@')

print('------ Fim do Programa ------')
