"""
Exercício Python 73: 
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do São Paulo.
"""
brasileirao = ("Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "Internacional", "São Paulo", "Bahia", 
               "Cruzeiro", "Vasco", "Atlético-MG", "Grêmio", "Vitória", "Corinthians", "Fluminense", "Criciúma", 
               "Bragantino", "Athletico-PR", "Juventude", "Cuiabá", "Atlético-GO")
cont = 1

print("-=" * 20)
print("{:^40}".format("BRASILEIRÃO - 07/11/2024"))
print("-=" * 20)

for t in brasileirao:
    print(cont,"-", t)
    cont += 1
print("\n")
print("-=" * 20)
print("{:^40}".format("CINCO PRIMEIROS TIMES"))
print("-=" * 20)

for t in brasileirao[:5]:
    print(t)

print("\n")
print("-=" * 20)
print("{:^40}".format("OS QUATRO ÚLTIMOS TIMES"))
print("-=" * 20)

for t in brasileirao[-4:]:
    print(t)
print("\n")

print("-=" * 20)
print("{:^40}".format("TIMES EM ORDEM ALFABÉTICA"))
print("-=" * 20)

for t in sorted(brasileirao):
    print(t)
print("\n")

print("-=" * 20)
print("{:^40}".format("POSIÇÃO DO TIME DO SÃO PAULO"))
print("-=" * 20)
print(f"O time do São Paulo está na posição: {brasileirao.index("São Paulo")+1}º colocado.")
print("\n")