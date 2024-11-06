"""
Exercício Python 68: 
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep
vit = 0

while True:
    sleep(0.5)
    comp = randint(0, 10)
    print("\nO computador escolheu um número")
    num = int(input("Insira o seu número para saber quem vencerá: "))

    soma = comp + num
    tipo = " "

    while tipo not in "PI":
        tipo = str(input("Escolha PAR ou ÍMPAR [P/I]: ")).strip().upper()[0]

    print(f"Você digitou {num} e o computador digitou {comp}", end=", ")
    print("deu PAR!!" if soma % 2 == 0 else "deu ÍMPAR!!")


    if tipo == "P":
        if soma % 2 == 0:
            print("Parabéns você VENCEU!!")
            vit += 1
        
        else:
            print("Você PERDEU!!")
            break

    elif tipo == "I":
        if soma % 2 == 1:
            print("Parabéns você VENCEU!!")
            vit += 1
        
        else:
            print("Você PERDEU!!")
            break

    print("Vamos jogar novamente...")

print(f"Você venceu {vit} vezes.\n")