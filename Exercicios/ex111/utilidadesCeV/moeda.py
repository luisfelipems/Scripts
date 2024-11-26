def aumentar(preco = 0, taxa = 0, formato=False):
    resp =  preco + (preco * taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preco = 0, taxa = 0, formato=False):
    resp = preco - (preco * taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preco = 0, formato=False):
    resp = preco * 2
    return resp if formato is False else moeda(resp)


def metade(preco = 0, formato=False):
    resp = preco / 2
    return resp if formato is False else moeda(resp)

def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxab=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxab}% de redução: \t{diminuir(preco, taxab, True)}')
    print('-' * 40)
