#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quatidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m**2

larg = float(input("Digite a largura da parede (METROS): "))
alt = float(input("Digite a altura da parede (METROS): "))
area = larg*alt
qntd_tinta = area/2
print("Largura: {} \nAltura: {} \nÁrea: {}m² \nQuantidade de latas de tinta necessária para pintá-la: {}l"
      .format(larg, alt, area, qntd_tinta))

