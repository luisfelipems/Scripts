"""
Exercício Python 090: 
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()

aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['média'] = float(input(f"Digite a média do aluno {aluno["nome"]}: "))

if aluno['média'] >= 7:
    aluno['situação'] = "Aprovado"

elif 5 <= aluno['média'] < 7:
    aluno['situação'] = "Recuperação"

else:
    aluno['situação'] = "Reprovado"

print(aluno)