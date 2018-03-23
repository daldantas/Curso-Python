n = int(input("Digite um nº: "))
p = 0
for c in range(2, n):
    if n % c == 0:
        p += 1
print("Não primo" if p != 0 else "É primo")
