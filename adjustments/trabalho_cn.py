import numpy as np
import pandas as pd

# Definindo a função f(Q)
def f(Q, C):
    return C * np.exp(Q) - 4 * Q**2

# Função phi(Q) para o método do ponto fixo
def phi(Q, C):
    return np.sqrt(C * np.exp(Q) / 4)

# Método do ponto fixo
def ponto_fixo(C, Q0, tol=1e-4, max_iter=100):
    Q = Q0
    iteracoes = []
    for i in range(max_iter):
        novo_Q = phi(Q, C)
        iteracoes.append((i + 1, Q, novo_Q, abs(novo_Q - Q)))
        if abs(novo_Q - Q) < tol:
            return novo_Q, iteracoes
        Q = novo_Q
    return Q, iteracoes

# Derivada de f(Q)
def df(Q, C):
    return C * np.exp(Q) - 8 * Q

# Método de Newton modificado
def newton_mod(C, Q0, tol=1e-4, max_iter=100):
    Q = Q0
    iteracoes = []
    for i in range(max_iter):
        novo_Q = Q - f(Q, C) / df(Q, C)
        iteracoes.append((i + 1, Q, novo_Q, abs(novo_Q - Q)))
        if abs(novo_Q - Q) < tol:
            return novo_Q, iteracoes
        Q = novo_Q
    return Q, iteracoes

# Método da secante original
def secante(C, Q0, Q1, tol=1e-4, max_iter=100):
    iteracoes = []
    for i in range(max_iter):
        fQ0 = f(Q0, C)
        fQ1 = f(Q1, C)
        novo_Q = Q1 - fQ1 * (Q1 - Q0) / (fQ1 - fQ0)
        iteracoes.append((i + 1, Q0, Q1, novo_Q, abs(novo_Q - Q1)))
        if abs(novo_Q - Q1) < tol:
            return novo_Q, iteracoes
        Q0, Q1 = Q1, novo_Q
    return novo_Q, iteracoes

# Entrada do usuário
C = float(input("Digite o valor de C: "))
Q0 = float(input("Digite o valor de Q0 (chute inicial): "))
Q1 = float(input("Digite o valor de Q1 (segundo chute inicial para o método da secante): "))

# Calcular Q usando os três métodos
root_fp, iteracoes_fp = ponto_fixo(C, Q0)
root_nm, iteracoes_nm = newton_mod(C, Q0)
root_sec, iteracoes_sec = secante(C, Q0, Q1)

# Exibir resultados
print(f"Raiz pelo método do ponto fixo: {root_fp}")
df_iteracoes_fp = pd.DataFrame(iteracoes_fp, columns=['Iteração', 'Q', 'novo_Q', 'Erro'])
print(df_iteracoes_fp)

print(f"\nRaiz pelo método de Newton modificado: {root_nm}")
df_iteracoes_nm = pd.DataFrame(iteracoes_nm, columns=['Iteração', 'Q', 'novo_Q', 'Erro'])
print(df_iteracoes_nm)

print(f"\nRaiz pelo método da secante: {root_sec}")
df_iteracoes_sec = pd.DataFrame(iteracoes_sec, columns=['Iteração', 'Q0', 'Q1', 'novo_Q', 'Erro'])
print(df_iteracoes_sec)
