valorProduto = float(input("Valor do produto: "))
modoPgto = int(input("Digite o número que corresponde ao modo de pagamento:\n0 - à vista (dinheiro ou cheque)\n1 - à vista (cartão)\n2 - até 2x (cartão)\n3 - 3x (cartão) ou mais \n"))
if modoPgto == 0:
    desc = valorProduto * .1
    print("Desconto de R${:.2f} (10%), pagará o total de R${:.2f}.".format(desc, valorProduto - desc))
elif modoPgto == 1:
    desc = valorProduto * .05
    print("Desconto de R${:.2f} (5%), pagará o total de R${:.2f}.".format(desc, valorProduto - desc))
elif modoPgto == 2:
    print("Sem desconto e sem acréscimo, pagará o total de R${:.2f}.".format(valorProduto))
elif modoPgto == 3:
    acrescimo = valorProduto * .2
    print("Acrécimo de R$ {:.2f} (20%), pagará o total de R${:.2f}.".format(acrescimo, valorProduto + acrescimo))
else:
    print("Este número não corresponde a um modo de pagamento.")