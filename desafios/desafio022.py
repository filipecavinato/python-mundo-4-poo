# Script criado por Filipe Cavinato

from rich import print
from rich.panel import Panel
import os

class ControleRemoto:
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 2

    def controle(self):
        while True:
            if not self.ligado:
                conteudo = f':prohibited: A TV está desligada'
            else:
                conteudo = f'''Canal = {"[on blue] 1 [/]" if self.canal == 1 else " 1 "} {"[on blue] 2 [/]" if self.canal == 2 else " 2 "} {"[on blue] 3 [/]" if self.canal == 3 else " 3 "} {"[on blue] 4 [/]" if self.canal == 4 else " 4 "} {"[on blue] 5 [/]" if self.canal == 5 else " 5 "}
Volume = {"[on green] [/]" * int(self.volume)}{"[on white] [/]" * (10 - int(self.volume))}'''
            painel = Panel(conteudo, title=' [ TV ] ', width=35)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(painel)
            opcao = str(input(f'< CH{self.canal} >   - Vol{self.volume} +  '))
            if opcao == '@' and not self.ligado:
                self.ligado = True
            elif opcao == '@' and self.ligado:
                self.ligado = False
            elif opcao in '+-' and self.ligado:
                self.ajustar_volume(opcao)
            elif opcao in '<>' and self.ligado:
                self.mudar_canal(opcao)
            if opcao == '0':
                break

    def ajustar_volume(self, comando):
        if comando == '+':
            if self.volume < 10:
                self.volume += 1
        elif comando == '-':
            if self.volume > 2:
                self.volume -= 1

    def mudar_canal(self, comando):
        if comando == '>':
            if self.canal < 5:
                self.canal += 1
            elif self.canal >= 5:
                self.canal = 1
        elif comando == '<':
            if self.canal > 1:
                self.canal -= 1
            elif self.canal <= 1:
                self.canal = 5

# Código Principal
c1 = ControleRemoto()
c1.controle()
