"""
Exercício Python 095: 
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização 
de detalhes do aproveitamento de cada jogador.
"""

"""
Exercício Python 093: 
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o 
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f"Quantas partidas o {jogador['Nome']} jogou? "))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c+1}? ")))

    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]

        if resp in "SN":
            break
        print('ERRO! \nResponda apenas S ou N.')

    if resp == "N":
        break

print('-=' * 30)
print('COD ', end = "")
for i in jogador.keys():
    print(f'{i:<15}', end = "")
print()

print('-=' * 40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()
print('-=' * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))

    if busca == 999:
        break
    
    if busca >= len(time):
        print("ERRO! \nNão existe jogador com o código digitado.")

    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}: ")
        for i, g in enumerate(time[busca]['Gols']):
            print(f' No jogo {i+1} fez {g} gols.')
    print('-' * 40)

print("<< VOLTE SEMPRE!!! >>>")