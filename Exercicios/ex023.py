"""
Exercício 23:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

numero = int(input("Por favor, insira um número de 0 a 9.999: "))

u = numero // 1 % 1
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("A unidade deste número é {}".format(u))
print("A dezena deste número é {}".format(d))
print("A centena deste número é {}".format(c))
print("A milhar deste número é {}".format(m))