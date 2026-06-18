# Script criado por Filipe Cavinato

from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo = None, total_paginas = None):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1
        self.paginas_viradas = 0
        print(f':book:[blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.total_paginas}[/] páginas'
              f' no total. Você está na [yellow]página {self.pagina_atual}[/][/]')

    def avancar_pagina(self, paginas_viradas):
        self.paginas_viradas = paginas_viradas
        pagina_atual = self.pagina_atual
        contador = 0
        if self.pagina_atual <= self.total_paginas:
            while self.pagina_atual < paginas_viradas + pagina_atual and self.pagina_atual < self.total_paginas:
                self.pagina_atual += 1
                contador += 1
                print(f'Pág{self.pagina_atual} -> ', end='')
                sleep(0.5)
            if self.pagina_atual <= self.total_paginas:
                print(f'[blue]Você avançou {contador} páginas e agora está na [yellow]página {self.pagina_atual}[/][/]')
            if self.pagina_atual == self.total_paginas:
                print(f'[red]:rotating_light: Você chegou ao final do livro {self.titulo}[/]')

l1 = Livro('10 Coisas que aprendi', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(100)

print('------ Fim do Programa ------')
