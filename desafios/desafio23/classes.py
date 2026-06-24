# Modulo criado por Filipe Cavinato

from abc import ABC, abstractmethod
from math import pow, pi

class Poligono(ABC):
    def __init__(self, quantidade_lados):
        self.quantidade_lados = quantidade_lados

    @abstractmethod
    def perimetro(self):
        pass
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(quantidade_lados = 4)
        self.lado = lado

    def perimetro(self):
        return self.quantidade_lados * self.lado

    def area(self):
        return pow(self.lado, 2)


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(quantidade_lados = 1)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * pow(self.raio,2)

