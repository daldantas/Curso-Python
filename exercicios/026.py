# 026
f = str(input("Frase: "))
qa = f.count('a')
ppa = f.find('a') + 1
pua = f.rfind('a') + 1
print("\n Quantidade de Aparições de 'a': {} \n Posição Primeira Aparição de 'a': {} \n Posição Última Aparição de 'a': {}".format(qa, ppa, pua))