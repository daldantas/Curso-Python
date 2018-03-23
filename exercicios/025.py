# 025
print("<Com if>")
n = str(input("Nome completo: ").lower())
if n.find('silva') > -1:
    print("Tem Silva")
else:
    print("Não tem Silva")
# 025 sem if
print("<Sem if>")
n = str(input("Nome completo: ").lower())
print("silva" in n)