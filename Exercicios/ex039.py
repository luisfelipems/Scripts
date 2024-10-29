"""
Exercício Python 39: 
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

atual = date.today().year
ano = int(input("Por favor, insira o seu ano de nascimento: "))
idade = atual - ano

if idade < 18:
    print("Você tem {} anos em {}.".format(idade, atual))
    print("Ainda faltam {} ano(s) para o seu alistamento.".format(18-idade))
    print("Você precisa se alistar em: {}".format(atual+(18-idade)))
elif idade == 18:
    print("Você tem {} anos no em {}.".format(idade, atual))
    print("Você precisa se alistar este ano!!")
else:
    print("Você tem {} anos em {}.".format(idade, atual))
    print("Você passou do prazo de alistamento em {} ano(s)!!!".format(idade-18))
    print("Você deveria ter se alistado em: {}".format(atual-(idade-18)))