# Algoritmo que lê o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite seu salário R$:"))
aumento = salario * 1.15
print("Seu salário R${}, seu salário com o aumento de 15%, R${:.2f}".format(salario, aumento))

