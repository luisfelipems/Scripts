"""
Exercício 17:
Faça um programa que leia o compimento do cateto
oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""

from math import sqrt

CO = float(input("Por favor, insira o valor do cateto oposto: "))
CA = float(input("Por favor, digite o valor do cateto adjacente: "))

hipotenusa = sqrt((CO ** 2) + (CA ** 2)) #sqrt método para calcular a raiz quadrada

print("O valor da hipotenusa é de: {:.2f}".format(hipotenusa))