# Script criado por Filipe Cavinato

from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços', width=30)

tabela.add_column('Nome', justify='right', style='bold red')
tabela.add_column('Preço', justify='center', style='bold blue')

tabela.add_row('Lápis', 'R$ 1,50')
tabela.add_row('Computador', '[green]R$ 4.500,00[/]')

print(tabela)

print('------ Fim do Programa ------')
