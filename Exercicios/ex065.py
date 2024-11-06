"""
Exercício Python 65: 
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário 
se ele quer ou não continuar a digitar valores.
"""
status = 's'
num = cont = soma =  0

while status == 's':
    num = int(input("Digite um número: "))
    cont += 1
    soma += num

    if cont == 1:
        maior = menor = num

    if num >= maior:
        maior = num
    
    elif num <= menor:
        menor = num

    status = str(input("Deseja continuar? Digite S/N: ")).lower().strip()[0]

print("Você digitou {} numeros. \nA média dos números inseridos foi de {:.2f} \nO maior número foi o {}. \nO menor número foi o {}".format(cont, soma / cont, maior, menor))