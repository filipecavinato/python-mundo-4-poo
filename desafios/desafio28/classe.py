# Classe criada por Filipe Cavinato

from rich import print

class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 == 0:
            if 16 <= valor <= 30:
                self.__temperatura = valor
            elif valor < 16:
                self.__temperatura = 16
            else:
                self.__temperatura = 30
        else:
            print(f'[red] ERRO: Temperatura de {valor}ºC é Inválida![/]')
        return self.__temperatura
