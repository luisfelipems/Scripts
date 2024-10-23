"""
Exercício 16:
Crie um programa que leia um número real qualquer pelo teclado e mostre
na tela a sua porção inteira.
"""
from math import floor

numero = float(input("Por favor, digite o valor desejado: "))
novonum = floor(numero)

print("O número arredondado é: {}".format(novonum))