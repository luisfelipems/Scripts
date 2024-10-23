"""
Exercício 18:
Faça um programa que leia um ângulo qualquer e mostre na tela o valor
de seno, cosseno e tangente dese ângulo.
"""
import math

angulo = int(input("Por favor, insira número do ângulo: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print("O angulo é {} \nO SENO é {:.2f}\nO COSSENO é {:.2f} \nE a TANGENTE é {:.2f}".format(angulo, sen, cos, tang))