# Classe criada por Filipe Cavinato

from rich import print

class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id          # Publico
        self._titular = nome  # Protegido
        self.__saldo = saldo  # Privado
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R$ {self.__saldo:,.2f}')

    def __str__(self):
        return f'Estado Atual da Conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R$ {valor:,.2f} [green]Autorizado[/] na conta {self.id}')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'Saque de R$ {valor:,.2f} [red]NEGADO[/]. [yellow]Saldo Insuficiente[/]')
        else:
            self.__saldo -= valor
            print(f'Saque de R$ {valor:,.2f} [green]Autorizado[/] na conta {self.id}')
