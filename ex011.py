#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quatidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m**2

larg = int(input("Digite a largura da parede (METROS): "))
alt = int(input("Digite a altura da parede (METROS): "))
area = larg*alt
qntd_tinta = area/2
print("Largura: {} \nAltura: {} \nÁrea: {} \nQuantidade de tinta necessária para pintá-la: {}"
      .format(larg, alt, area, qntd_tinta))

