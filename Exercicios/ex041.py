"""
Exercício Python 041: 
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date
atual = date.today().year

nasc = int(input("Insira o ano de nascimento do atleta: "))
idade = atual - nasc

if idade <= 9:
    print("A idade do atleta é {} e a categoria dele é MIRIM.".format(idade))
elif idade > 9 and idade <= 14:
    print("A idade do atleta é {} e a categoria dele é INFANTIL.".format(idade))
elif idade > 14 and idade <= 19:
    print("A idade do atleta é {} e a categoria dele é JÚNIOR.".format(idade))
elif idade > 19 and idade <= 25:
    print("A idade do atleta é {} e a categoria dele é SÊNIOR.".format(idade))
else:
    print("A idade do atleta é {} e a categoria dele é MASTER.".format(idade))