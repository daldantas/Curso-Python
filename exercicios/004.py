# coding=utf-8
algo = input('Digite algo: ')
print(
    '\n Tipo: ', type(algo),
    '\n Alfanumérico: ', algo.isalnum(),
    '\n Alfa: ', algo.isalpha(),
    '\n Numérico: ', algo.isnumeric(),
    '\n Maiúsculas: ', algo.isupper(),
    '\n Espaço: ', algo.isspace()
)