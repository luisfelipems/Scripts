"""
Exercício Python 099: 
Faça um programa que tenha uma função chamada maior(), que receba vários 
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e 
dizer qual deles é o maior.
"""
from time import sleep

def maiorValor( * num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')

    for valor in num:
        print(f'{valor}', end=" ", flush=True)
        sleep(0.3)
        cont +=1

        if cont == 0:
            maior = valor
        
        if valor > maior:
            maior = valor
    print(f'\nForam informados {cont} números;')
    print(f'O maior valor é o {maior}.')


maiorValor(2, 9, 4, 5, 7, 1)
maiorValor(4, 7, 0 )
maiorValor(1, 2)
maiorValor(6)
maiorValor()