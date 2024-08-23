# Elabore um pseudocódigo que receba a distância percorrida (km) e a quantidade de combustível utilizada (litros) para exibir o consumo médio do carro.

km = float(input("digite a distância: "))
litro = float(input("digite a quantidade de combustível: "))
print("Seu consumo foi: {0:.2f}".format(km/litro))