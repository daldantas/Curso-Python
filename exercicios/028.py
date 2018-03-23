from random import choice
i = [0, 1, 2, 3, 4, 5]
c = choice(i)
uc = int(input("Adinvinhe, digite um número entre 0 e 5."))
if c == uc:
    print('Eita cagão, Acertou!')
else:
    print("Errou, o numero correto é ",c," tente novamente.")