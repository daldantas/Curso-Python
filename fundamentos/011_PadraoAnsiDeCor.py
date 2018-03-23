print("\033[31;40mEste é um título com cor alterada usando o código ANSI\033[m")
print("\033[1;30;46mEste é um título com cor alterada usando o código ANSI\033[m")

x = "alterada"
print("{}Este é um título com cor {} {}{} {}usando o código{}".format('\033[30;46m', '\033[4;34m', x, '\033[m', '\033[30;46m','\033[m'))