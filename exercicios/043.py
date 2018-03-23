peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / altura**2
if imc < 18.5:
    print("\033[33mIMC({:.2f}) - Abaixo do peso ideal.\033[m".format(imc))
elif imc >= 18.5 and imc < 25:
    print("\033[32mIMC({:.2f}) - Peso ideal.\033[m".format(imc))
elif imc >= 25 and imc < 30:
    print("\033[33mIMC({:.2f}) - Sobrepeso.\033[m".format(imc))
elif imc >=30 and imc <= 40:
    print("\033[31mIMC({:.2f}) - Obesidade.\033[m".format(imc))
else:
    print("\033[30;41mIMC({:.2f}) - Obesidade mórbida.\033[m".format(imc))