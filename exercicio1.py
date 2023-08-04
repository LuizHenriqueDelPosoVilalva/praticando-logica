'''Escreva um programa que receba um número inteiro do usuário e determine se esse número é par ou ímpar. 
O programa deve imprimir "PAR" se o número for par e "ÍMPAR" se for ímpar.'''

numero = int(input('Digite um numero inteiro: '))

if numero % 2 == 0:
    print("PAR")
else:
    print("ÍMPAR")