"""
Exercício Python 57: 
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

SEXO = ""

while SEXO != "F" and SEXO != "M":
    SEXO = str(input("Digite o sexo da pessoa com M (Masculino) ou F (Feminino): ")).upper().strip()
    print("Sexo digitado inválido, por favor insira novamente.")
    print(SEXO)

print("O sexo digitado foi: {}".format(SEXO))