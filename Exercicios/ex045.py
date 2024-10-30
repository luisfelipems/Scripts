"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print("""Suas opções:
        [1] PEDRA 
        [2] PAPEL 
        [3] TESOURA """)

jogador = int(input("Qual é a sua jogada? "))-1

print("-="*15)
print("VOCÊ JOGOU {}".format(itens[jogador]))
print("O COMPUTADOR JOGOU {}".format(itens[computador]))
print("-="*15)

if computador == 0:
    if jogador == 0:
        print("EMPATE!!!")

    elif jogador == 1:
        print("JOGADOR VENCE!!")

    elif jogador == 2:
        print("COMPUTADOR VENCE!!")

    else:
        print("Jogada inválida!!")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR {} VENCE!!".format())

    elif jogador == 1:
        print("EMPATE!!!")

    elif jogador == 2:
        print("JOGADOR VENCE!!")
    else:
        print("Jogada inválida!!")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!!")

    elif jogador == 1:
        print("COMPUTADOR VENCE!!")

    elif jogador == 2:
        print("EMPATE!!!")

    else:
        print("Jogada inválida!!")
