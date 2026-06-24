# Modulo criado por Filipe Cavinato

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome ='', salario_bruto = 0):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = 0
        self.salario_minimo = 1612
        self.inss = 7.5

    def analisar_salario(self):
        conteudo = f'O Salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R$ {self.salario:,.2f}[/] e corresponde a [yellow]{self.salario/self.salario_minimo:.1f} Salários Mínimos[/].'
        painel = Panel(conteudo, title='Análise de Salário', width=50)
        print(painel)

    @abstractmethod
    def calculo_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calculo_salario(self):
        self.salario_bruto = (self.valor_hora * self.horas_trabalhadas)
        self.salario = self.salario_bruto - ((self.inss/100) * self.salario_bruto)
        return self.salario

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto)

    def calculo_salario(self):
        self.salario = self.salario_bruto - ((self.inss/100) * self.salario_bruto)
        return self.salario
