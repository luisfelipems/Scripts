"""
Exercício Python 078: 
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual 
foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
maior = menor = 0

for c in range(0, 5):
    valores.append(int(input(f"Insira um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = valores[c]

    if valores[c] >= maior:
        maior = valores[c]
    
    elif valores[c] <= menor:
        menor = valores[c]
    
print(f"\nVocê digitou os números: {valores[:]}")
print(f"O maior valor digitado é o {maior} na posição: ", end=" ")
for p, v in enumerate(valores):
    if v == maior:
        print(f"{p} ", end="")

print(f"\nO menor valor digitado é o {menor} na posição: ", end=" ")
for p, v in enumerate(valores):
    if v == menor:
        print(f"{p} ", end="")