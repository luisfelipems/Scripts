"""
Exercício Python 8: 
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
valor = float(input("Por favor, digite a metragem desejada: "))

print("A metragem é {0}, o valor em centímetros é {1} e o valor em milímetros é {2}".format(valor, valor*100, valor*1000))