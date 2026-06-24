# Script criado por Filipe Cavinato

from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('José', 17, 'Informatica', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario('Claudia', 27, 'Secretária', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()

    print('------ Fim do Programa ------')

if __name__ == '__main__':
    main()
