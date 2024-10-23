"""
Exercício Python 4: 
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
valor = input("Digite algo: ")

print("O valor digitado foi {}".format(valor))
print("O valor é do tipo ", type(valor))
print("É numérico? ", valor.isnumeric())
print("É alpha? ", valor.isalpha())
print("É Alphanumérico? ", valor.isalnum())
print("Está tudo em maíusculo? ", valor.isupper())
print("Está tudo em minúsculo? ", valor.islower())
print("A primeira é maíscula? ", valor.istitle())