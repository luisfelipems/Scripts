"""
Exercício Python 098: 
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, 
fim e passo. Seu programa tem que realizar três contagens através da função criada: 
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    if inicio < fim:
        print(f"\nContagem de {inicio} até {fim} em {1}:")
        for num in range(inicio, fim, 1):
            print(num, end=" ", flush=True)
            sleep(0.5)
        print("FIM!!!")
   
    else:
        print(f"\nContagem de {inicio} até {fim} em {passo}:")
        for num in range(inicio, fim, -passo):
            print(num, end=" ", flush=True)
            sleep(0.5)
        print("FIM!!!")

contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é a sua vez inserir a contagem: ")
ini = int(input("Inicio: "))
final = int(input("Fim: "))
pas = int(input("Passo: "))

contador(ini, final, pas)