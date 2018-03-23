vel = float(input("Digite a velocidade: "))
if vel > 80:
    i = vel - 80
    m = 7*i
    print("Você foi multado em R$ {:.2f}".format(m))
