# Modulo criado por Filipe Cavinato

from abc import ABC, abstractmethod
from rich import print
from random import choice, randint

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        print(f'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com [blue]{choice(self.golpes)}[/] de força {forca}')
        dano = randint(0, forca)
        alvo.receber_dano(dano)
        print(f'[blue]{alvo.nome}[/] recebeu dano de [red]{dano}[/]!')

    def receber_dano(self, dano):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Pulo Giratório', 'Arremesso Preciso', 'Redemoinho do Caos']

    def curar(self):
        cura = randint(0, 100)
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.')
        self.vida += cura

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Tornado de Fogo', 'Raio de Gelo', 'Míssil Magico']

    def curar(self):
        cura = randint(0,100)
        print(f'[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.')
        self.vida += cura
