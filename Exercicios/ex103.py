"""
Exercício Python 103: 
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros 
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz 
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado 
corretamente.
"""

def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeanto.')

#Programa principal
jogador = str(input("Digite o nome do jogador: "))
gol = str(input("Digite o número de gols: "))

if gol.isnumeric():
    gol = int(gol)

else:
    gol = 0

if jogador.strip() == "":
    ficha(gols = gol)

else:
    ficha(jogador, gol)