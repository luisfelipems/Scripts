"""
Exercício Python 105: 
Faça um programa que tenha uma função notas() que pode receber várias notas de 
alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas, maior nota, menor nota, média da turma, situação (opcional)
"""

def notas(* n, sit=False):
    """_summary_
    Função para analisar notas e situação de um aluno.
    Args:
        n = qualquer quantidade de notas
        sit = situação que só aparecerá se o valor for True, o default é False.
        return = retorna um dicionário com todas as notas, média e situação do aluno. 
    """
    r = dict()

    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'

        else:
            r['situação'] = 'RUIM'

    return r                     

resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)