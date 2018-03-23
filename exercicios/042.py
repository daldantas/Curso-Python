r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print("\033[32mEquilátero.\033[m")
    elif r1 == r2 or r3 == r1 or r2 == r3:
        print("\033[32mIsósceles.\033[m")
    else:
        print("\033[32mEscaleno.\033[m")
else:
    print("\033[31mEstas medidas não forma um triângulo.\033[m")