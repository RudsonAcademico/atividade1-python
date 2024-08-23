"""
Suponha que um caixa eletrônico disponha apenas de notas de 1, 10 e 50 reais.
Considerando que o cliente está querendo fazer um saque de um valor qualquer (considere esse valor inteiro).
Faça um algoritmo que mostre o número mínimo de notas que o caixa deve fornecer para o cliente.
Mostre também, o valor do saque, e a quantidade de cada nota a ser entregue.
Obs: O caixa não trabalha com moedas
"""

valor=int(input("Digite o valor do saque: "))
n1=0
n10=0
n50=0
tnotas=0

print("O Valor total é do saque é {}".format(valor))

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
