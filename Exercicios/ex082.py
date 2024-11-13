"""
Exercício Python 082: 
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas 
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao 
final, mostre o conteúdo das três listas geradas.
"""

lista = []
pares = []
impares = []

while True:
    lista.append(int(input("Digite um número: ")))
    resp = str(input("Deseja continuar? [S/N] "))
    
    if resp in "Nn":
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)

    else:
        impares.append(n)

print(f"Lista completa: {lista}")
print(f"Lista com números pares: {pares}")
print(f"Lista com números ímpares: {impares}")