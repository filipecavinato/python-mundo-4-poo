# Script criado por Filipe Cavinato

# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Metodo Construtor
        #Atributo de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()
print(g2.mensagem())

print('------ Fim do Programa ------')
