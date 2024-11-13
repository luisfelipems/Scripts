"""
Exercício Python 074: 
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre 
a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("Os número sorteados foram: ", end="")

for n in num:
    print(n, end=" ")

print(f"\nO maior número sorteado foi o {max(num)}")
print(f"O menor número sorteado foi o {min(num)}")