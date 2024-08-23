valor=int(input("Digite o valor do saque: "))
n1=0
n10=0
n50=0
tnotas=0

print("O Valor total é do saque é{}".format(valor))

if valor >= 50:
    n50 = valor // 50
    tnotas+=n50
    valor%=50
if valor >= 10:
    n10 = valor // 10
    tnotas+=n10
    valor%=10
if valor >= 1:
    n1 = valor
    tnotas+=n1
print("""
O valor total de notas é: {}
A quantidade de notas de 50 é: {}
A quantidade de notas de 10 é: {}
A quantidade de notas de 1 é: {}            
""".format(tnotas,n50,n10,n1))
