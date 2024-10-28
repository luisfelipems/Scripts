"""
Exercício Python 36: 
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

VALOR_CASA = float(input("Por favor, digite o valor do imóvel: "))
VALOR_SALARIO = float(input("Agora insira o valor do seu salário: R$"))
TEMPO = int(input("Agora insira a quatidade de meses a ser financiado: "))

PARCELA_FINANCIAMENTO = VALOR_CASA / TEMPO
PERCENTUAL_SALARIO = VALOR_SALARIO * 0.30

if PARCELA_FINANCIAMENTO <= PERCENTUAL_SALARIO:
    print("Financiamento aprovado com as seguintes condições: \nValor do imóvel: R${:.2F}\nPrazo do financiamento: {} \nValor da parcela do financiamento: R${:.2F}".format(VALOR_CASA, TEMPO, PARCELA_FINANCIAMENTO))
else:
    print("Financiamento não foi aprovado pois o valor da parcela excete o limite de 30% do seu salário: R${:.2F}\nPrazo do financiamento: {} \nValor da parcela do financiamento: R${:.2F} \nSalario: R${:.2F} \nParcela máxima disponível com o seu salário: R${}".format(VALOR_CASA, TEMPO, PARCELA_FINANCIAMENTO, VALOR_SALARIO, PERCENTUAL_SALARIO))