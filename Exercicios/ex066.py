"""
Exercício Python 66: 
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
num = soma = qtd = 0

while True:
    num = int(input("Insira um número inteiro, para interromper digite 999: "))
    
    if num == 999:
        break

    soma += num
    qtd += 1

print(f"A quantidade de números inseridos foi: {qtd} \nA soma entre eles é: {soma}")