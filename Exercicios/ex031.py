"""
Exercício 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.
"""

km = int(input("Insira a distância em km: "))

if km <= 200:
    print("O valor da viagem será de R${:.2f}".format(float(km*0.50)))
else:
    print("O valor da viagem será de R${:.2f}".format(float(km*0.45)))