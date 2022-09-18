#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

mt = float(input("Digite um valor em metros: "))
km = mt/1000
hcm = mt/100
dm = mt/10
dcm = mt*10
ct = mt*100
mm = mt*1000

print("{} metros \n\nVALOR CONVERTIDO PARA QUILÔMETRO, HECTÔMETRO, DECÂMETRO, ".format(mt), end = "")
print("DECÍMETRO, CENTÍMETRO E MILÍMETRO")
print("\n{}km\n{}hcm\n{}dm\n{}dcm\n{}ct\n{}mm".format(km, hcm, dm, dcm, ct, mm))





