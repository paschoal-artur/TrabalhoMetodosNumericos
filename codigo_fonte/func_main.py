import numpy as np

# Função que calcula o custo de produção
def f(Q, C):
    return C*np.exp(Q) - 4*Q**2 

# Insere os dados no banco de dados
def insert_db(C, k, x0, x1, db):
    db['k'].append(k)
    db['Q0'].append(round(x0, 5))
    db['Q1'].append(round(x1, 5))
    db['Custo'].append(round(f(x1, C), 5))
    db['Erro'].append(round(abs(x1 - x0), 5))

def viabilidade(r):
    if r > 0.7:
        return 'Inviável'
    else:
        return 'Viável'