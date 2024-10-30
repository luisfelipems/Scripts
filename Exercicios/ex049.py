"""
Exercício Python 49: 
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.
"""
from time import sleep

numero = int(input("Digite o número que deseja saber a tabuada: "))

print("A tabuada do número {} é:".format(numero))
print("-="*5)
for c in range(1,11):
    print("{}x{} = {}".format(numero, c, numero*c))
    sleep(0.2)
print("-="*5)