"""
Exercício Python 69: 
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
nome = ""
idade = 0
masculino = 0
maioridade = 0
feminino = 0

while True:
    nome = str(input("Digite o nome da pessoa: ")).strip()
    idade =  int(input("Digite a idade da pessoa: "))
    sexo = " "

    while sexo not in "MF":
        sexo = str(input("Digite o sexo da pesso M/F: ")).strip().upper()[0]
    
    if idade >= 18:
        maioridade += 1

    if sexo == "M":
        masculino += 1

    if sexo == "F" and idade < 20:
         feminino += 1
    
    resp = " "

    while resp not in "SN":
        resp = str(input("Deseha continuar? S/N: ")).strip().upper()

    if resp == "N":
        break        

print(f"Há {maioridade} com mais de 18 anos. \nHá {masculino} homens cadastrados. \nHá {feminino} mulheres que tem menos de 20 anos.")