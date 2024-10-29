"""
Exercício Python 42: 
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais;
- ISÓSCELES: dois lados iguais, um diferente;
- ESCALENO: todos os lados diferentes;
"""
r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Primeira reta: {} \nSegunda reta: {} \nTerceira reta: {} \nCom elas é possível formar um triângulo ".format(r1, r2, r3), end="")

    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO!!")

    elif r1 != r2 != r3 != r1:
        print("ESCALENO!!")
    
    else:
        print("ISÓSCELES!!")
    
else:
    print("As retas digitadas foram: {}, {} e {}. Com elas não é possível formar um triângulo.".format(r1, r2, r3))