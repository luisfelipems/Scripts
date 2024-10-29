"""
Exercício Python 44: 
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 
preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal 
- 3x ou mais no cartão: 20% de juros
"""

VALOR = float(input("Insira o valor do produto: R$"))

print(""" Formas de pagamento:
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão""")

OPCAO = int(input("Insira a opção de pagamento desejada: "))

if OPCAO == 1:
    VALOR_FINAL = VALOR * 0.90
    print("Opção de pagamento à vista dinheiro/cheque: \nO valor do produto que era de R$ {:.2f} ficará R$ {:.2f} com o desconto aplicado.".format(VALOR, VALOR_FINAL))

elif OPCAO == 2:
    VALOR_FINAL = VALOR * 0.95
    print("Opção de pagamento à vista cartão: \nO valor do produto que era de R$ {:.2f} ficará R$ {:.2f} com o desconto aplicado.".format(VALOR, VALOR_FINAL))

elif OPCAO == 3:
    VALOR_FINAL = VALOR
    print("Opção de pagamento em até 2x no cartão: R${:.2f}\nPreço formal o valor do produto R$ {:.2f}".format(VALOR/2,VALOR, VALOR_FINAL))

elif OPCAO == 4:
    VALOR_FINAL = VALOR * 1.2
    print("Opção de pagamento 3x ou mais no cartão: \nO valor do produto que era de R$ {:.2f} ficará R$ {:.2f} com o juros aplicado.".format(VALOR, VALOR_FINAL))

else:
    print("Opção inválida de pagamento!!!")