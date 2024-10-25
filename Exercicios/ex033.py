"""
Exercício 33:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O maior númerio digitado foi o primeiro: {}".format(n1))
elif n2 > n1 and n2 >n3:
    print("O maior número digitado foi o segundo: {}".format(n2))
elif n3 > n1 and n3 > n2:
    print("O maior número digitado foi o terceiro: {}".format(n3))