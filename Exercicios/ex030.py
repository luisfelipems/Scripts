"""
Exercício 30:
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
"""

numero = int(input("Insira um número: "))

if numero % 2 == 0:
    print("O número digitado foi {} e ele é par.".format(numero))
else:
    print("O numero digitado foi {} e ele é impar.".format(numero))