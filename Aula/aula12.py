"""
Estrutura de condição aninhada:

"""

nome = str(input("Qual é o seu nome?"))

if nome == "Luis":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Pedro":
    print("Seu nome é bem popular no Brasil!")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome femino!")
else:
    print("Seu nome é bem normal.")

print("Tenha um bom dia, {}!".format(nome))
