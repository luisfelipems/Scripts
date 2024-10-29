"""
Exercício Python 43: 
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa 
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso;
- Entre 18,5 e 25: Peso Ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade Mórbida;
"""

peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso / (altura ** 2)

print("O seu IMC é {:.2f} e você está ".format(imc), end="")

if imc < 18.5:
    print("abaixo do peso.")

elif imc >= 18.5 and imc < 25:
    print("peso ideal.")

elif imc >= 25 and imc < 30:
    print("sobrepeso.")

elif imc >= 30 and imc < 40:
    print("obesidade.")

else:
    print("obesidade mórbida.")