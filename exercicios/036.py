valorCasa = float(input("Valor da casa: "))
salario = float(input("Seu salário: "))
tempoPgtoAno = int(input("Pagará em quantos anos: "))
tempoPgtoMes = tempoPgtoAno * 12
valorMaxPar = salario * .3
valorPar = valorCasa / tempoPgtoMes

if valorPar > valorMaxPar:
    print("\033[31mEmpréstimo negado.\033[m")
else:
    print("\033[32mEmpréstimo liberado.\033[m")
    print("\033[32m{} parcelas de R$ {:.2f}".format(tempoPgtoMes, valorPar),"\033[m")