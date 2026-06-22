# Script criado por Filipe Cavinato

from rich import print

class Funcionario:
    """
    Cria um Funcionário que tem nome, setor, cargo e permite ele se apresentar.
    """
    # Atributo de Classe
    empresa = 'Curso em Video'

    def __init__ (self, nome = None, setor = None, cargo = None):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentar())
c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentar())

print('------ Fim do Programa ------')
