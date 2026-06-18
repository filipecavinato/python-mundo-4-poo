# Script criado por Filipe Cavinato

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
        print(f'Deposito de R$ {valor:,.2f} \033[32mAutorizado\033[m na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de R$ {valor:,.2f} \033[31mNEGADO\033[m. \033[33mSaldo Insuficiente\033[m')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} \033[32mAutorizado\033[m na conta {self.id}')

c1 = ContaBancaria(112, 'Gustavo', 3000)

c1.depositar(500)
c1.sacar(2000)
c1.sacar(1000000)
print(c1)

print('------ Fim do Programa ------')
