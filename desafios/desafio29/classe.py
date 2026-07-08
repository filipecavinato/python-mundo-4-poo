# Classe criada por Filipe Cavinato

from rich import print

class Diario:
    def __init__(self, senha_mestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senha_mestra

    def escrever(self, mensagem):
        self.__segredos.append(mensagem)

    def ler(self, senha = None):
        if senha == self.__senha:
            print('[green] DIÁRIO LIBERADO![/]')
            for segredo in self.__segredos:
                print(f'- {segredo}')
        else:
            print('[red] Senha Invalida! Você não pode ler o meu Diário[/]')

