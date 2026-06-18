# Script criado por Filipe Cavinato

from rich import print

class Funcionario:
    """
    Cria um Funcionário uqe tem nome, setor e cargo e permite ele se apresentar.
    """
    def __init__ (self, nome = None, setor = None, cargo = None):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = 'Curso em Video'

    def apresentar(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentar())
c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentar())

print('------ Fim do Programa ------')
