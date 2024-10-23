""" 
Exercício 15:
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$ 60,00 por dia e R$ 0,15 por KM rodado.
"""
dias = int(input("Por favor, digite o número de dias que o carro foi alugado: "))
km = float(input("Por favor, agora insira qual a kilometragem rodada com o carro: "))
total = (dias * 60) + (0.15 * km)

print("O total devido é de R${}".format(total))