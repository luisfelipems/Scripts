"""
Exercício Python 10: 
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""
real = float(input("Por favor, insira o valor disponível em carteira: "))
dolar = 3.27

print("O valor em reais é de R$ {0:.2f} e o valor após a converção para dolar é de $ {1:.2f}".format(real, real/dolar))