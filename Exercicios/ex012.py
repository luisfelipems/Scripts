"""
Exercício Python 12: 
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco = float(input("Por favor, insira o preço do produto desejado: "))

print("O preço do produto é de R${0:.2f} e o valor após o desconto é de: R${1:.2f}".format(preco, preco*0.95))