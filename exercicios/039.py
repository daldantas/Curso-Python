from datetime import datetime
print("="*10," SITUAÇÃO COM O SERVIÇO MILITAR ","="*10)
anoNasc = int(input("\033[30mDigite o seu ano de nascimento: \033[m"))
anoAtual = datetime.now().year

# Evita um ano bizarro
if anoNasc > anoAtual:
    exit(print("\033[31mAno de nascimento não pode ser maior que o ano corrente\033[m"))
if anoNasc < anoAtual - 125:
    exit(print("\033[31mImpossível ter mais de 125 anos\033[m"))
# fim Evita um ano bizarro

idade = anoAtual - anoNasc
difer = idade - 18

# Plural ou singular?
if difer == 1 or difer == -1:
    wordAno = "ano"
elif difer > 1 or difer < -1:
    wordAno = "anos"
# fim Plural ou singular?

if difer > 0:
    print("\033[31mPassou do tempo, você devia ter se alistado {} {} atrás.\033[m".format(difer, wordAno))
elif difer < 0:
    print("\033[32mAinda vai se alistar, daqui {} {}.\033[m".format(difer * -1, wordAno))
else:
    print("\033[33mHora de se alistar, você deve se alistar este ano.\033[m")
print("="*43)