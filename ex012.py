#Faça um algoritmo que leia o preço de um produto e mostr seu novo preço, com 5% de desconto.

preco = float(input("Preço do produto R$:"))
desconto = preco * 0.95
print("O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}".format(preco, desconto))


