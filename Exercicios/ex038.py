"""
Exercício Python 038: 
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

PRIMEIRO_VALOR = int(input("Insira o primeiro valor: "))
SEGUNDO_VALOR = int(input("Insira o segundo valor: "))

if PRIMEIRO_VALOR > SEGUNDO_VALOR:
    print("O primeiro valor: {} é maior que o segundo valor: {}".format(PRIMEIRO_VALOR, SEGUNDO_VALOR))

elif SEGUNDO_VALOR > PRIMEIRO_VALOR:
    print("O segundo valor: {} é maior que o primeiro valor: {}".format( SEGUNDO_VALOR, PRIMEIRO_VALOR))

else:
    print("O primeiro e segundo valor são iguais: {}".format(PRIMEIRO_VALOR))