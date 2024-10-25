"""
Exercício 29:
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80 Km/h, motre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

km = int(input("Insira a velocidade em Km/h: "))

if km > 80:
    print("Você foi multado pois estava acima do limite de velocidade permitido! \nO valor da multa é de R${:.2f}".format((float(km-80))*7))
else:
    print("Você estava dentro do limite permitido de velocidade: {}Km/h.".format(km))