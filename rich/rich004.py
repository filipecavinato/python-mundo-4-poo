# Script criado por Filipe Cavinato

from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R$ {self.saldo:,.2f}')

    def __str__(self):
        return f'A Conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R$ {valor:,.2f} [green]Autorizado[/] na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de R$ {valor:,.2f} [red]NEGADO[/] ([yellow]Saldo Insuficiente[/])')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} [green]Autorizado[/] na conta {self.id}')

c1 = ContaBancaria(111, 'José', 3000)

inspect(c1)
print(c1)
print(c1.__getstate__())

print('------ Fim do Programa ------')
