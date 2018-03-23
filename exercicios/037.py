print("="*10," Conversor de bases ","="*10)
n = int(input("Digite um nº: "))
b = int(input("Digite o nº que corresponde a base desejada\n1 para Binário\n2 para Octal\n3 para Hexadecimal\n"))

if b == 1:
    c = bin(n)
    print("Binário de {} é {}".format(n, c))
elif b == 2:
    c = oct(n)
    print("Octal de {} é {}".format(n, c))
elif b == 3:
    c = hex(n)
    print("Hexadecimal de {} é {}".format(n, c))
else:
    print("\033[31mEste número não corresponde a uma base.\033[m")

