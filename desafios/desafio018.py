# Script criado por Filipe Cavinato

from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        consumo_padrao = 0.400
        preco_carne_kilo = 82.40
        quant_carne = self.quant * consumo_padrao
        preco_total = quant_carne * preco_carne_kilo
        preco_pessoa = preco_total / self.quant

        conteudo = f'''Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]
Cada Participante comerá {consumo_padrao}Kg e cada Kg custa R${preco_carne_kilo:.2f}
Recomendo [blue]comprar {quant_carne:.3f}Kg[/] de carne
O custo total será de [green]R${preco_total:.2f}[/]
Cada pessoa pagará [yellow]R${preco_pessoa:.2f}[/] para participar.'''
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()

c2 = Churrasco('Churras dos Amigos 2ª Parte', 100)
c2.analisar()

print('------ Fim do Programa ------')
