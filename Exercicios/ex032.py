"""
Exercício 32:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto
"""

ano = int(input("Por favor, digite o ano para saber se ele é bisexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano inserido é {} e ele é bissexto.".format(ano))
else:
    print("O ano digitado é {} e ele não é bissexto.".format(ano))