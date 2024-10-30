"""
Exercício Python 48: 
Faça um programa que calcule a soma entre todos os números que são 
múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

print("A soma dos números que são múltiplos de três entre 1 e 500 é: {}".format(soma))
print("Há {} que foram somados neste intervalo.".format(cont))