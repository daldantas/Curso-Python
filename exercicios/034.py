s = float(input("Salário: "))
if s >1250:
    a = s * .1
    ns = s + a
else:
    a = s * .15
    ns = s + a
print("Aumentou em R$ {:.2f}".format(a)," e foi atualizado para em R$ {:.2f}".format(ns))