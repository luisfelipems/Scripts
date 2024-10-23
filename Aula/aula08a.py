"""Importe de bibliotecas - Aula de módulos"""
# import math - importa toda a biblioteca 
# from math import floor - importa apenas o floor da biblioteca math
from math import sqrt
import random

num = int(input("Digite um número: "))
raiz = sqrt(num) # sqrt = raiz quadrada
teste = random.randint(1,100)

# math.ceil arredontamento de número float para cima e math.floor para baixo
print("A raiz de {} é igual a {:.2f}".format(num, raiz)) 
print(teste)
