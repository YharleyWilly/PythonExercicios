""" Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado. """

km = float(input("Informe a quantidade de Km percorridos pelo carro: "))
dia = int(input("Informe a quantidade de dias pelos quais o veículo foi alugado: "))
preco = (60 * dia) + (km * 0.15)
print("O preço a pagar será de R${:.2f}".format(preco))

