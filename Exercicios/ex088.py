"""
Exercício Python 088: 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos 
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
composta.
"""
from random import randint
from time import sleep

lista = list()
jogos = list()

print("-" * 30)
print("-=" * 2,f" JOGO DA MEGA SENA ", "-=" * 2)
print("-" * 30)

qntd = int(input("Quantos jogos você quer fazer? "))
tot = 0

while tot < qntd:
    cont = 0

    while True:
        num = randint(1, 60)
        
        if num not in lista:
            lista.append(num)
            cont += 1

        if cont >= 6:
            break

    lista.sort()   
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print("-=" * 3, f" SORTEANDO {qntd} JOGOS ", "-=" * 3)

for i,  jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
    sleep(1)

print("-=" * 5, " BOA SORTE !!! ", "-=" * 5 )