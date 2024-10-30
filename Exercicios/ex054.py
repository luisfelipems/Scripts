"""
Exercício Python 54: 
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    
    nasc = int(input("Digite o ano de nascimento da pessoa {}: ".format(pess)))
    idade = atual - nasc

    if idade >= 18:
        totmaior += 1
        
    else:
        totmenor += 1

print("Ao todo tivermos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))