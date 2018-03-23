n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
top = ' Início '
bot = ' Fim '
print('\n Operadores Aritméticos \n')
print('{:=^30}'.format(top))
print('\n Soma: {} \n Mult: {} \n div : {:.2f} \n divi: {} \n expo: {}'.format(s, m, d, di, e), end='')
print('\n rest: {} \n'.format(r))
print('{:=^30}'.format(bot))