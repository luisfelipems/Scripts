"""
Exercício 16:
Crie um programa que leia um número real qualquer pelo teclado e mostre
na tela a sua porção inteira.
"""
from math import trunc # trunc tranforma o número real para número inteiro

numero = float(input("Por favor, digite o valor desejado: "))
print("O valor digitado é {} e o arredondamento é: {}".format(numero, trunc(numero)))