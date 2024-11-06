"""
Exercício Python 67: 
Faça um programa que mostre a tabuada de vários números, um de cada vez, para 
cada valor digitado pelo usuário. O programa será interrompido quando o número 
solicitado for negativo.
"""
from time import sleep

num = 0

while True:
    num = int(input("Digite o número da tabuada que você deseja saber: "))
    if num < 0:
        break
    
    print('-'*20)
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
        sleep(0.2)
    print('-'*20)
    
    if num != 0:
        print("Para continuar digite o próximo número, para sair digite um valor negativo.")
        sleep(2)
        
print("Programa da tabuada encerrado. Obrigado!!")