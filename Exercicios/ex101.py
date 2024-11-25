"""
Exercício Python 101: 
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano

    if idade < 16:
        return f"Idade: {idade}, VOTO NEGADO!!!"
    
    elif idade >= 16 and idade < 18 or idade > 65:
        return f"Idade: {idade}, VOTO OPICIONAL!!!"
    
    else:
        return f"Idade: {idade}, VOTO OBRIGATÓRIO!!!"
    

resp = int(input("Digite o ano de nascimento: "))

print(voto(resp))
