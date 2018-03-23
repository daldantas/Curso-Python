n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
m = (n1 + n2) / 2
if m > 6.949:
    print("\033[32mMédia {:.1f}, está APROVADO.\033[m".format(m))
elif m < 4.959:
    print("\033[31mMédia {:.1f}, está REPROVADO.\033[m".format(m))
else:
    print("\033[33mMédia {:.1f}, está em RECUPERAÇÃO.\033[m".format(m))