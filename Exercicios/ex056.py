"""
Exercício Python 56: 
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres 
têm menos de 20 anos.
"""
MEDIA_IDADE = 0
SOMA_IDADE = 0
HOMEM_MAISVELHO = ""
HOMEM_MAISVELHOIDADE = 0
QNTD_MULHERES = 0


for i in range(1, 5):

    NOME = str(input("Insira o nome: ")).strip()
    IDADE = int(input("Insira a idade: "))
    SEXO = str(input("M ou F: ")).upper().strip()
    SOMA_IDADE += IDADE

    if i == 1 and SEXO == "M":
        HOMEM_MAISVELHO = NOME
        HOMEM_MAISVELHOIDADE = IDADE

    if SEXO == "M" and IDADE > HOMEM_MAISVELHOIDADE:
        HOMEM_MAISVELHO = NOME
        HOMEM_MAISVELHOIDADE = IDADE
    
    if SEXO == "F" and IDADE < 20:
        QNTD_MULHERES =+1

MEDIA_IDADE += SOMA_IDADE / 4

print("A média de idade é de {} anos".format(MEDIA_IDADE))
print("O homem mais velho tem {} anos e se chama {}.".format(HOMEM_MAISVELHOIDADE,HOMEM_MAISVELHO))
print("Ao todo são {} mulheres com menos de 20 anos.".format(QNTD_MULHERES))