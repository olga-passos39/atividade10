# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.

numero = float(input('Digite um número para saber se é par ou impar:'))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
     print('Número é impar')