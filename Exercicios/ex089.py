"""
Exercício Python 089: 
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
de cada aluno individualmente.
"""
aluno = list()

while True:
    nome = str(input("Digite o nome do aluno: "))
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    media = (n1+n2)/2

    aluno.append([nome, [n1, n2], media])

    if str(input("Deseja continuar? [S/N] ")) in "Nn":
        break

print("-=" * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-" * 26)

for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:

    print("-" * 35)
    opcao = int(input("Motrar notas  de qual aluno? (999 interrompe): "))

    if opcao == 999:
        print("FINALIZANDO...")
        break

    if opcao <= len(aluno) - 1:
        print(f"Nota de {aluno[opcao][0]} são {aluno[opcao][1]}")

print("<<< VOLTE SEMPRE >>>")