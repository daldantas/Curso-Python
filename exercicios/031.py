dis = float(input("Distância em km: "))
if dis <= 200:
    v = dis * .5
else:
    v = dis * .45
print("Vai custar R$ {:.2f}".format(v))