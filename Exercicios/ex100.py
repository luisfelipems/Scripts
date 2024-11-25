"""
Exercício Python 100: 
Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares 
sorteados pela função anterior.
"""
from random import randint
from time import sleep

def sorteia(lista):

    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)

    somaPar(lista)

def somaPar(lista):
    soma = 0

    for n in lista:
        if n % 2 == 0:
            soma += n

    print(f'\nA soma dos números pares de {lista} é: {soma}')

numeros = list()

sorteia(numeros)