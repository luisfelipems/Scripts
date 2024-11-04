"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

opcao = 0

print("-="*6)
print("CALCULADORA")
print("-="*6)

n1 = int(input("Por favor, insira o primeiro valor: "))
n2 = int(input("Por favor, insira o segundo valor: "))

while opcao != 5:
    sleep(2)
    opcao = int(input("\n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa \n \nSelecione a operação desejada: "))

    if opcao == 1:
        sleep(2)
        print("\nVocê escolheu 1 - SOMAR: ")
        print("O resultado da soma de {} + {} é: {}".format(n1, n2, n1+n2))
    
    elif opcao == 2:
        sleep(2)
        print("\nVocê escolheu 2 - MULTIPLICAR: ")
        print("O resultado da multiplicação de {} x {} é: {}".format(n1, n2, n1*n2))
    
    elif opcao == 3:
        sleep(2)
        print("\nVocê escolheu 3 - MAIOR: ")

        if n1 > n2:
            print("O maior número é o {}".format(n1))

        elif n2 > n1:
            print("O maior número é o {}".format(n2))
        
        else:
            print("Os dois números são iguais: {} e {}.".format(n1, n2))

    elif opcao == 4:
        sleep(1)
        print("\nVocê escolheu 4 - NOVOS NÚMEROS")

        n1 = int(input("Por favor insira o primeiro número novamente: "))
        n2 = int(input("Por favor insira o segundo número novamente: "))
    
    elif opcao == 5:
        sleep(1)
        print("\nVocê escolheu 5 - SAIR DO PROGRAMA \nObrigado e volte sempre!!!")
    
    else:
        sleep(2)
        print("\nOpção inválida, por favor selecione uma opções entre 1 e 5.")