print('1.0 Litro pinta 2.0 m²')
lar = float(input("Largura: "))
alt = float(input("Altura: "))
are = lar * alt
lit = are / 2
print('{:.2f} Litros = {:.2f} m² '.format(lit, are))