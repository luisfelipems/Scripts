"""
Exercício 22:
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maíusculas
* O nome com todas as letras minísculas
* Quantas letras ao todo tem (sem considerar espaços)
* Quantas letras tem o primeiro nome """

nome = str(input("Por favor, digite o seu nome completo: "))

print("Nome em maísculo: {}".format(nome.upper()))
print("Nome em minisculo: {}".format(nome.lower()))
print("Quantidade de caracteres sem considerar o espaço: {}".format(len(nome) - nome.count(" ")))
print(nome.find(" "))