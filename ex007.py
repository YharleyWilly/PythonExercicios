#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nota1 = float(input('Primeira nota: '))
nota2 =float(input('Segunda nota: '))
média = (nota1+nota2)/2
print('Sua média é: {:.1f}'.format(média))

# {:.1f} significa que o número será representado com um dígito após o ponto (FLOAT)

