"""
Exercício Python 087: 
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))
        

print("-=" * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")

        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]

        if coluna == 2:
            scol += matriz[linha][coluna]

        if linha == 1:
            if matriz[linha][coluna] > mai:
                mai = matriz[linha][coluna]

    print()

print("-=" * 30)
print(f"A soma de todos os números pares da matriz é: {spar}")
print(f"A soma dos números da terceira coluna da matriz é: {scol}")
print(f"O maior valor da segunda linha é o: {mai}\n")