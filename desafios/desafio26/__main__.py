# Script criado por Filipe Cavinato

from classes import FuncionarioHorista, FuncionarioMensalista
from rich.panel import Panel

def main():
    f1 = FuncionarioHorista('Paulo', 12, 200)
    f1.calculo_salario()
    f1.analisar_salario()

    f2 = FuncionarioMensalista('Amanda', 9500)
    f2.calculo_salario()
    f2.analisar_salario()

if __name__ == '__main__':
    main()