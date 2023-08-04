'''Crie um programa que calcule a soma de todos os números inteiros de 
1 a N, onde N é um número inteiro fornecido pelo usuário.'''

numero = int(input("Digite o numero inteiro: "))

def somaDeTodosOsNumerosInteiros (numero):
    numeros = range(1, numero+1)
    soma = 0

    for i in numeros:
        soma +=i
    return soma
        

resultado = somaDeTodosOsNumerosInteiros(numero)
print(resultado)
        