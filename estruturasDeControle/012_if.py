nomesFem = "Marjorie Helena Maia Janaina Elisabete"
nomesCom = "Maria José Beatriz João"
nomeBon = "Gabriel"
nome = str(input("Digite seu primeiro nome: "))
if nome == nomeBon:
    print(nome, "é um lindo nome")
elif nome in nomesFem:
    print(nome, "é um nome feminino muito bonito")
elif nome in nomesCom:
    print(nome, "é um nome muito comum no Brasil")
else:
    print(nome, "é um nome normal")