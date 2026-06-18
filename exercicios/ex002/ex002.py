# Script criado por Filipe Cavinato

# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem um nome e idade.
    Para criar uma nova pessoa use:
    → variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = 'Vazio', idade = 0): # Metodo Construtor
        #Atributo de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de Objetos
g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1)
print(g1.__getstate__())

g2 = Gafanhoto('Mauro', 53)
g2.aniversario()
print(g2)
print(g2.__getstate__())

g3 = Gafanhoto()
print(g3)
print(g3.__getstate__())

print(g1.__class__)

print('------ Fim do Programa ------')
