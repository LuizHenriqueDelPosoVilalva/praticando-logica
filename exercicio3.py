'''Exercício 3: Escreva um programa que peça ao usuário para digitar uma palavra e, 
em seguida, imprima a palavra invertida. Por exemplo, se o usuário digitar "python", 
o programa deve imprimir "nohtyp".'''

palavra = (input("Digite a palavra que deseja reverter: "))

def invertString (palavra):
  listaDeLetras = list(palavra)
  rev = reversed(listaDeLetras)
  stirngFinal = ''.join(rev)

  return stirngFinal

resultado = invertString(palavra)
print(resultado)

