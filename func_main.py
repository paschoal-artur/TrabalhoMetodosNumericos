import numpy as np

def f(Q, C):
    try:
        return C*np.exp(Q) - 4*Q**2
    except OverflowError:
        return float('inf') 

def df(Q, C):
    return C * np.exp(Q) - 8 * Q