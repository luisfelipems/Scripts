"""
Exercício Python 55: 
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input("Insira o peso da pessoa {}: ".format(i)))

    if i == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print("O MAIOR peso digitado foi: {}".format(maior))
print("O MENOR peso digitado foi: {}".format(menor))