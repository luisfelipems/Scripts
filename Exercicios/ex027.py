"""
Exercício Python 27: 
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o 
primeiro e o último nome separadamente.
"""

n = str(input("Por favor, digite o seu nome completo: ")).strip()
nome = n.split()

print("O seu primeiro nome é: {}".format(nome[0]))
print("E o seu último nome é: {}".format(nome[len(nome)-1]))