#Exercício de classificar tipo primitivo do valor e identificar a variável.

dgt = input('Digite algo: ')
print('O tipo primitivo é: {}'.format(type(dgt)))
print('Só tem espaços? {}'.format(dgt.isspace()))
print('É alfabético? {}'.format(dgt.isalpha()))
print('É um número? {}'.format(dgt.isnumeric()))
print('Tem número e letra? {}'.format(dgt.isalnum()))
print('É decimal?', dgt.isdecimal())
print('Está em maiúsculo? {}'.format(dgt.isupper()))
print('Está em minúsculo?', dgt.islower())















