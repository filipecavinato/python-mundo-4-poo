# Modulo criado por Filipe Cavinato

from abc import ABC, abstractmethod
from math import pow, pi

class Poligono(ABC):
    def __init__(self, quantidade_lados):
        self.quantidade_lados = quantidade_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(quantidade_lados = 4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.quantidade_lados * self.lado

    def area(self) -> float:
        return pow(self.lado, 2)


class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(quantidade_lados = 0)
        self.raio = raio

    def perimetro(self) -> float:
        return 2 * pi * self.raio

    def area(self) -> float:
        return pi * pow(self.raio,2)
