import numpy as np

def f(Q, C):
    return C*np.exp(Q) - 4*Q**2 

def df(Q, C):
    ''' Parameters
    Q: Valor atual de Q
    C: Constante utilizada na função `f`
    '''
    #! Derivada da função `f(Q)` em relação a Q
    return C * np.exp(Q) - 8 * Q