# Script criado por Filipe Cavinato

from classe import Diario
from rich import inspect, print

def main():
    d = Diario()
    d.escrever('Primeira Mensagem')
    d.escrever('Você é uma pessoa simpática')
    d.escrever('Você gosta de Python')
    try:
        print(d.senha)
    except PermissionError as erro:
        print(f'[red] ERRO: {erro}[/]')

    try:
        d.ler(str(input('Digite a senha para ler o diario: ')).strip())
    except PermissionError as erro:
        print(f'[red] ERRO: {erro}[/]')

    try:
        print(f'[yellow]Alterando a senha[/]')
        d.senha = str(input('Digite a nova senha: '))
    except PermissionError as erro:
        print(f'[red] ERRO: {erro}[/]')

    try:
        d.ler(str(input('Digite a senha para ler o diario: ')).strip())
    except PermissionError as erro:
        print(f'[red] ERRO: {erro}[/]')

    #inspect(d, private=True, methods=True)   # Analise da Classe usando inspect

if __name__ == '__main__':
    main()
