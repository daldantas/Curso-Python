# Lógica concisa para a decisão:
from random import choice
from time import sleep
loop = True
while loop == True:
    print("="*12," J O K E N P Ô ","="*12)
    print(" "*15, "PEDRA = 0, PAPEL = 5, TESOURA = 2\n", "="*33)
    joks = (0, 1, 2)
    itens = ('\033[36mPEDRA\033[m', '\033[34mPAPEL\033[m', '\033[35mTESOURA\033[m')
    jokCPU = choice(joks)
    jokPlayer = int(input("Sua jogada: "))
    if jokPlayer == 5:
        jokPlayer = 1
    if jokPlayer in joks:
        result = jokPlayer - jokCPU

        # LÓGICA CONCISA
        if result == 1 or result == -2:
            result = "Vitória"
            cor = "\033[32m"
        elif result == -1 or result == 2:
            result = "Derrota"
            cor = "\033[31m"
        elif result == 0:
            result = "Empate"
            cor = "\033[33m"
        # FIM LÓGICA CONCISA

        print(" \033[30;46mJ O\033[m ")
        sleep(.7)
        print(" \033[30;44mK E N\033[m ")
        sleep(.7)
        print(" \033[30;45mP Ô\033[m  ")
        sleep(.3)
        print(cor,result,"\033[m")
        print("Jogada do player: {}\nJogada do CPU: {}\n".format(itens[jokPlayer], itens[jokCPU]))
    else:
        print("\033[31mEscolha um número que corresponda a uma jogada (0, 5 ou 2).\033[m")