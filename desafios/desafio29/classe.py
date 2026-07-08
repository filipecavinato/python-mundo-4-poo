# Classe criada por Filipe Cavinato

from rich import print

class Diario:
    def __init__(self, senha_mestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senha_mestra.strip()

    def escrever(self, mensagem):
        if isinstance(mensagem, str) and len(mensagem) > 0:
            self.__segredos.append(mensagem)

    def ler(self, senha = None):
        if senha == self.__senha:
            print('[green] DIÁRIO LIBERADO![/]')
            for segredo in self.__segredos:
                print(f'- {segredo}')
        else:
            raise PermissionError('Senha Invalida! Você não pode ler o meu Diário.')

    @property
    def senha(self):
        raise PermissionError(f'Ninguém tem permissão de ver a senha')

    @senha.setter
    def senha(self, nova_senha):
        senha_antiga = str(input('Digite a senha atual para confirmar: ')).strip()
        if senha_antiga == self.__senha:
            self.__senha = nova_senha
        else:
            raise PermissionError(f'Senha Atual Invalida, você não pode alterar a senha!')

