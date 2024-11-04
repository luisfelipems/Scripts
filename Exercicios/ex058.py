"""
Exercício Python 58: 
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.

Exercício 28:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 6 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint

computador = randint(0, 10)
status = False
cont = 0

numero = int(input("O computador escolheu um número, insira um número entre 0 e 10 para saber se você acertou: "))

while not status:

    cont += 1

    if numero < computador:
        print("O número é maior...")
    elif numero > computador:
        print("O número é menor...")

    if numero == computador:
        print("\nO número escolhido pelo computador foi: {} \nVocê escolheu: {} \nParabéns, você acertou!! ".format(computador, numero))
        status = True    
    elif cont != 0:
        numero = int(input("Não foi dessa vez, tente novamente: "))
        
print("Você advinhou o número escolhido pelo computador em {} vez(es)!!!\n".format(cont))