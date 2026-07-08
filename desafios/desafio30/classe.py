# Classe criada por Filipe Cavinato

from hashlib import sha256
from rich import print

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        senha_hash = sha256(senha.encode('utf-8')).hexdigest()
        self.__hash = senha_hash

    def validar(self, tentativa):
        tentativa_hash = sha256(tentativa.encode('utf-8')).hexdigest()
        if tentativa_hash == self.__hash:
            print('Senha Confere!')
            return True
        else:
            print(f'Senha não bate!')
            return False

