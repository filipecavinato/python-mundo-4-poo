# Script criado por Filipe Cavinato

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.lista = []

    def add_favoritos(self, favorito):
        favoritos = favorito
        self.lista.append(':video_game: ' + f'[blue]{favoritos}[/]')
        return self.lista

    def ficha(self):
        conteudo = f'''Nome Real: {self.nome}
Jogos Favoritos:'''
        conteudo2 = '\n'.join(sorted(self.lista))

        painel = Panel(f'{conteudo}\n{conteudo2}',title=f'Jogador <{self.nick}>', width=44)
        print(painel)

j1 = Gamer('Fabricio da Silva', 'detonator2025')
j1.add_favoritos('Mario Bros')
j1.add_favoritos('Sonic')
j1.add_favoritos('God Of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.add_favoritos('Mario Bros')
j2.add_favoritos('Call Of Duty')
j2.ficha()

print('------ Fim do Programa ------')
