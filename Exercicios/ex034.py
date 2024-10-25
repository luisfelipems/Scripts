"""
Exercício 034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
Para salários inferiores ou iguais o aumento é de 15%
"""

salario = float(input("Por favor, insira o salário desejado: "))

if salario > 1250:
    print("O salario digitando foi de: R${:.2f} e o valor com o aumento de 10% é de R${:.2f}".format(salario, salario*1.10))
else:
    print("O salario digitando foi de: R${:.2f} e o valor com o aumento de 15% é de R${:.2f}".format(salario, salario*1.15))