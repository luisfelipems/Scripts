"""
Exercício Python 092: 
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

pessoa = {'Nome': str(input("Digite o seu nome: ")), 
          'Ano de Nascimento': int(input("Digite o ano de nascimento: ")), 
          'Carteira de Trabalho': int(input("Digitre o número da carteira de trabalho (Digite 0 se não houver): "))}

pessoa['Idade'] = datetime.now().year - pessoa['Ano de Nascimento']

if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de contratação'] = int(input("Insira o ano de contratação: "))
    pessoa['Salário'] =  float(input("Digite o salário da pessoa: "))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de contratação'] + 35) - datetime.now().year)


print("\n", "-=" * 5, " DADOS DA PESSOA ", "-=" * 5 )
for chave, dados in pessoa.items():
    print(f"{chave}: {dados}")