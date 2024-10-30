"""
Exercício Python 53: 
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando 
os espaços. Exemplos de palíndromos:
- Apos a sopa
- A sacada da casa
- Atorre da derrota
- O lobo ama o bolo
- Anotaram a data da maratona
"""

frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print("Temo um palíndromo!!")

else:
    print("A frase digitada não é um palíndromo!!")