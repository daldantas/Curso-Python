n1 = int(input("Digite um nº: "))
n2 = int(input("Digite outro nº: "))

if n1 > n2:
    print(n1, "é maior que", n2)
elif n2 > n1:
    print(n2, "é maior que", n1)
else:
    print(n1, "e", n2, "São iguais")