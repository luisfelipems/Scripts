"""
Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre: 
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
sair = "n"

while True:
    lista.append(int(input("\nInsira um número: ")))
    sair = str(input("Deseja sair? [S/N] "))
    
    if sair in "Ss":
        break

print("="*60)
print(f"Os números inseridos na lista foram: {lista}")
print(f"Você digitou {len(lista)} números.")

lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")

if 5 == lista:
    print("O valor 5 está nesta lista.")
    
else:
    print("O valor 5 não está nesta lista.")
