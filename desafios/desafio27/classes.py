# Modulo criado por Filipe Cavinato

from abc import ABC, abstractmethod
from rich import print
from random import choice, randint

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.golpes = []
        self.vivo = True

    def verifica_vida(self, alvo):
        if self.vida <= 0:
            self.vivo = False
        elif alvo.vida <= 0:
            alvo.vivo = False

    def atacar(self, alvo, forca):
        if self.vivo and alvo.vivo:
            print(
                f':crossed_swords: [green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com [blue]{choice(self.golpes)}[/] de força {forca}')
            dano = randint(0, forca)
            alvo.receber_dano(alvo, dano, forca)
            self.verifica_vida(alvo)

    def receber_dano(self, alvo, dano, forca):
        if self.vivo:
            if dano >= self.vida:
                self.vida = 0
            else:
                self.vida -= dano

        print(f':collision: [blue]{alvo.nome}[/] recebeu dano de [red]{dano}[/]! -> [red]{alvo.nome}({alvo.vida})[/]',
              end='')
        if dano == forca:
            print('([purple]Critical Hit[/])')
        else:
            print()

    def game_over(self, alvo):
        print(f'\n[bold yellow]Fim de Batalha![/]')
        if self.vivo:
            print(f':trophy: [green]{self.nome}[/] Venceu de :skull: [red]{alvo.nome}[/] :skull:')
        elif alvo.vivo:
            print(f':trophy: [green]{alvo.nome}[/] Venceu de :skull: [red]{self.nome}[/]')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Pulo Giratório', 'Arremesso Preciso', 'Redemoinho do Caos']

    def curar(self):
        if self.vivo:
            cura = randint(0, 100)
            if self.vida_max >= self.vida + cura:
                self.vida += cura
                print(
                    f':adhesive_bandage: [blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida. -> [green]{self.nome}({self.vida})[/]')

            else:
                self.vida = self.vida_max


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Tornado de Fogo', 'Raio de Gelo', 'Míssil Magico']

    def curar(self):
        if self.vivo:
            cura = randint(0, 100)
            if self.vida_max >= self.vida + cura:
                self.vida += cura
                print(
                    f':test_tube: [blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida. -> [green]{self.nome}({self.vida})[/]')
            else:
                self.vida = self.vida_max
