"""
Exercício Python 72: 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte' )

while True:
    num = int(input("Digite um número entre 0 e 20: "))

    if 0 <= num <= 20:
        break

    print("Tente novamente. ", end="")

print(f"Você digitou o número {cont[num]}")