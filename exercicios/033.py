n1 = int(input("Digite o 1º nº: "))
n2 = int(input("Digite o 2º nº: "))
n3 = int(input("Digite o 3º nº: "))
if n1 > n2:
    ma = n1
    me = n2
else:
    ma = n2
    me = n1
if n3 > ma:
    ma = n3
if n3 < me:
    me = n3
print("Maior: ",ma)
print("Menor: ",me)