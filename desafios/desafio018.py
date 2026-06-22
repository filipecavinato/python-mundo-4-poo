# Script criado por Filipe Cavinato

from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao:float = 0.400
    preco_carne_kilo:float = 82.40

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.participantes = quantidade

    def analisar(self):
        quant_carne = self.participantes * self.__class__.consumo_padrao
        preco_total = quant_carne * self.__class__.preco_carne_kilo
        preco_pessoa = preco_total / self.participantes

        conteudo = f'''Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]
Cada Participante comerá {self.__class__.consumo_padrao}Kg e cada Kg custa R${self.__class__.preco_carne_kilo:,.2f}
Recomendo [blue]comprar {quant_carne:.3f}Kg[/] de carne
O custo total será de [green]R${preco_total:,.2f}[/]
Cada pessoa pagará [yellow]R${preco_pessoa:,.2f}[/] para participar.'''
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()

c2 = Churrasco('Churras dos Amigos Parte 2', 100)
c2.analisar()

print('------ Fim do Programa ------')
