"""
Exercício 28:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 6 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint

num = randint(0,5)

numero = int(input("O computador escolheu um número, insira um número entre 0 e 5 para saber se você acertou: "))

if numero == num:
    print("O número escolhido pelo computador foi: {} e você escolheu: {} \nParabéns, você acertou!! ".format(num, numero))
else:
    print("O número escolhido pelo computador foi: {} e você escolheu: {} \nNão foi dessa vez.".format(num, numero))