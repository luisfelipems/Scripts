"""
Exercício Python 11: 
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
altura = float(input("Por favor, insira a altura em metros da parede a ser pintada: "))
largura = float(input("Por favor, agora insira a largura em metro da parede a ser pintada: "))

total = altura * largura

print("A quantidade de tinta para pintar a área desejada é de {0}".format(total/2))