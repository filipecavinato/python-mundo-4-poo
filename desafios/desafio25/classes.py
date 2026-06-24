# Modulo criado por Filipe Cavinato

from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia = 0, frete = 0):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia

    def calcular_frete(self):
        self.frete = self.distancia * self.__class__.fator
        return f'R$ [cian]{self.frete:,.2f}[/]'


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia

    def calcular_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * self.__class__.fator
            return f'R$ [cian]{self.frete:,.2f}[/]'
        else:
            return f'[yellow]Raio Mínimo de 50 Km[/]'


class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia

    def calcular_frete(self):
        if self.distancia <= 10:
            self.frete = self.distancia * self.__class__.fator
            return f'R$ [cian]{self.frete:,.2f}[/]'
        else:
            return f'[yellow]Raio Maximo de 10 Km[/]'
