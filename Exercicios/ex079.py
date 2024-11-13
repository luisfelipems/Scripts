"""
Exercício Python 079: 
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
únicos digitados, em ordem crescente.
"""
numeros = list()

while True:
    
    num = int(input("Digite um valor: "))
    if num not in numeros:
        numeros.append(num)
        print("Valor adicionado com sucesso!!")
    
    else:
        print("Este número já existe na lista, por favor digite novamente.")

    
    resp = str(input("Quer continuar? [S/N] ")).strip()
      
    if resp in "Nn":
            break

    elif resp != "S" and resp != "s":
            print("Por favor digite S para SIM ou N para NÃO.")

    
print("Você digitou os valores: ", end="")

numeros.sort()

for n in numeros:
    print(n, end=" ")