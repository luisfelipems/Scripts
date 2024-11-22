"""
Exercício Python 084: 
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
temp = list()
pessoas = list()
maiorpeso = menorpeso = 0

while True:
    temp.append(str(input("Digite o nome de uma pessoa: ")))
    temp.append(float(input("Digite o peso dessa pessoa: ")))

    if len(pessoas) == 0:
        maiorpeso = menorpeso = temp[1]
    
    elif temp[1] > maiorpeso:
        maiorpeso = temp[1]

    elif temp[1] < menorpeso:
        menorpeso = temp[1]

    pessoas.append(temp[:])
    temp.clear()

    if str(input("Deseja sair? [S/N] ")) in "Ss":
        break

print(f"\nA quantidade de pessoas cadastradas na lista é {len(pessoas)}")

print(f"O maior peso é o {maiorpeso}Kg. ", end="")
for p in pessoas:
    if p[1] == maiorpeso:
        print(f"[{p[0]}] ", end="")

print(f"\nO menor peso é o {menorpeso}Kg. ", end="")
for p in pessoas:
    if p[1] == menorpeso:
        print(f"[{p[0]}] ", end="")