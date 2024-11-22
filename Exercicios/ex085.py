"""
Exercício Python 085: 
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem 
crescente.
"""
lista = [[], []]
num = 0

for cont in range(1, 8):
    num = int(input(f"Insira o número {cont}: "))

    if num % 2 == 0:
        lista[0].append(num)

    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores impares digitados foram: {lista[1]}")