from math import hypot
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
#hi = (co**2 + ca**2) ** .5
hi = hypot(co, ca)
print("Hipotenusa: {:.2f}".format(hi))