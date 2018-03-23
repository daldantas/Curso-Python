km = float(input("Km rodados: "))
di = int(input("Em quantos dias: "))
to = di * 60 + km * .15
print("Total: R$ {:.2f}".format(to))