"""
Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
from Exercicios.ex111.utilidadesCeV import moeda

p = float(input("Digite o preço: R$"))
moeda.resumo(p, 20, 12)