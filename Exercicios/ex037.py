"""
Exercício Python 37:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

numero =  int(input("Digite o número que deseja realizar a conversão: "))
escolha = int(input("Para converter em binário insira o número 1 \nPara converter em octal insira o número 2 \nPara converter em hexadecimal digite 3. \nPor favor, digite a opção desejada: "))

if escolha == 1:
     print("A conversão do número {} para binário fica: {}".format(numero, bin(numero)[2:]))

elif escolha == 2:
    print("A conversão do número {} para octal fica: {}".format(numero, oct(numero)[2:]))

else:
    print("A conversão do número {} para hexadecimal fica: {}".format(numero, hex(numero)[2:]))