"""
Exercício Python 13: 
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input("Por favor insira o valor do salário atual: "))

print("O valor do salário atual é de R${0:.2f} e após a promoção, o valor foi para R${1:.2f}".format(salario, salario*1.15))