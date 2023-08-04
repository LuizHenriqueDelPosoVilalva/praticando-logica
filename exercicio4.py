'''Exercício 4: Crie um programa que receba um número inteiro do usuário e verifique se ele é um número primo. 
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.'''

# Se o numero for somente divisivel por 1 e ele mesmo, é primo, caso contrario, não.
numero = int(input('Digite um nomero: '))

def numeroPrimro (num):
    if num >= 1:
        for i in range(2, num):
            if num% i == 0:
                resultado = num, "não é primo"
                break
            else:
                resultado =num, "é primo"
    elif num == 0:
      resultado = num, "é zero"
    else:
      resultado = num, "é negativo"
    return resultado

verificacao = numeroPrimro(numero)
print(verificacao)


