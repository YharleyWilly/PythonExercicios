#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

mt = int(input('Digite um valor para ser lido em metros? '))
ct = int(mt*100)
ml = int(mt*1000)
print('{} metros\n{} centímetros\n{} milímetros'.format(mt, ct, ml))



