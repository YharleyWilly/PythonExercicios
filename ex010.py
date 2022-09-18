#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1.00=R$5.06

carteira = float(input("Digite a quantia disponível na sua carteira. USE PONTO (.) (##.###.##): "))
dol = (carteira*1)/5.06
print("Você pode comprar {} dólares".format(dol))


