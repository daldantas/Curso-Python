# coding=utf-8
frase = "Marjorie Helena minha pitchula!"
print(frase[9]) # se refere ao índice 9 da string
print(frase[9:15]) # do índice 9 ao 15
print(frase[12:22:2]) # :2 pula de 2 em 2
print(frase[:8]) # início ao 8
print(frase[9:]) # 9 ao Fim
print(frase[9::3]) # seleciona do 9 ao fim e dentro dessa seleçao pula de 3 em 3
print(len(frase)) # Comprimento
print(frase.count('e')) # mostra qtde de 'e' da frase
print(frase.count('e', 9, 15)) # mostra qtde de 'e' do 9 ao 15
print(frase.find('tchu')) # mostra onde 'tchu' começa
print(frase.find('Gabriel')) # retorna -1 quando não encontra
print('minha' in frase) # procura string na frase e retorna bool
print(frase.replace('pitchula', 'linda')) # substitui o 1º pelo 2º
print(frase.upper()) # deixa tudo maiúscula
print(frase.lower()) # deixa tudo minúscula
print(frase.capitalize()) # deixa a 1ª letra da frase maiúscula
print(frase.title()) # deixa a 1ª letra de cada palavra da frase em maiúscula
frase = "   Marjorie Helena minha pitchula!  "
print(frase)
print(frase.strip()) # remove espaços do início e do fim
print(frase.rstrip()) # remove espaços da direita "right"
print(frase.lstrip())# remove espaços da esquerda "left"
frase = frase.split() # explode do PHP "delimitador padrão é o espaço"
print(frase) # todos os índices
print(frase[1]) # 1º índice
print(frase[1][3]) # 3ª letra do 1º índice
frase = ' '.join(frase)# inverso do split
print(frase)
