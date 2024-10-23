"""
Exercício Python 7: 
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
nota1 = float(input("Por favor, digite a primeira nota: "))
nota2 = float(input("Por favor, digite a segunda nota: "))

print("A primeira nota deste aluno é {0}, a segunda nota deste aluno é {1} e a média das notas é {2}".format(nota1, nota2, (nota1+nota2)/2))