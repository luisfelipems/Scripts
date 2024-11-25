"""
Exercício Python 096: 
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
retangular (largura e comprimento) e mostre a área do terreno.
"""
def área(larg, comp):
    result = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {result}m²')


print(' Controle de Terrenos ')
print('-' * 30)
l = float(input("Digite a largura do terreno: "))
c = float(input("Digite o comprimento do terreno: "))

área(c, l)