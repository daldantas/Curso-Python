r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print("SIM, forma um triângulo.")
else:
    print("NÃO forma um triângulo.")