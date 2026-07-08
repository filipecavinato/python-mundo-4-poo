# Classe criada por Filipe Cavinato
from base64 import encode
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
        senha_mestra = sha256()
        senha_mestra.update(senha.encode('utf-8'))
        senha_hash = senha_mestra.hexdigest()
        self.__hash = senha_hash

    def validar(self, tentativa):
        senha_tentativa = sha256()
        senha_tentativa.update(tentativa.encode('utf-8'))
        hash_hex = senha_tentativa.hexdigest()

        if hash_hex == self.__hash:
            print('Senha Confere!')
            return True
        else:
            print(f'Senha não bate!')
            return False

