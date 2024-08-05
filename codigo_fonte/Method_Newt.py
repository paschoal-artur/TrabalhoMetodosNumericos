# Importando a biblioteca numpy para cálculos numéricos
import numpy as np

# Importando funções auxiliares do módulo `func_main`
from func_main import f, insert_db

# Função que calcula a derivada da função `f(Q)`
def df(Q, C):
    ''' Parameters
    Q: Valor atual de Q
    C: Constante utilizada na função `f`
    '''
    # Derivada da função `f(Q)` em relação a Q
    return C * np.exp(Q) - 8 * Q

# Função principal para o Método de Newton modificado
def newton_mod(C, x0, err, max_iter=100):
    ''' Parameters
    C: Constante utilizada na função `f` e sua derivada `df`
    x0: Chute inicial para o valor de Q
    err: Tolerância para a convergência
    max_iter: Número máximo de iterações permitidas
    '''
    
    # Inicializa um dicionário para armazenar os resultados do método
    newton_db = {
        'k': [],         # Iterações
        'Q0': [],        # Valor atual de Q (antes da iteração)
        'Q1': [],        # Valor próximo de Q (após a iteração)
        'Custo': [],     # Custo da iteração
        'Erro': []       # Erro da iteração
    }
    
    x1 = x0  # Define o chute inicial x0 como o valor atual x1

    # Verifica se o chute inicial x0 já está suficientemente perto de zero
    if abs(f(x0, C)) < err:
        # Se já estiver perto de zero, insere o resultado no banco de dados e retorna o valor e o dicionário
        insert_db(C, 0, x0, x1, newton_db)
        return x0, newton_db
    
    # Lista para armazenar as iterações (não utilizada no código, mas pode ser útil para depuração)
    iteracoes = []

    # Loop para realizar o método de Newton modificado até o número máximo de iterações
    for i in range(max_iter):
        # Calcula o próximo valor de Q usando o método de Newton
        x2 = x1 - f(x1, C) / df(x1, C)
        
        # Insere o resultado da iteração no banco de dados
        insert_db(C, i, x1, x2, newton_db)
        
        # Verifica se a solução está dentro do erro permitido ou se a mudança é pequena o suficiente
        if abs(f(x2, C)) < err or abs(x2 - x1) < err:
            # Se a solução for aceitável, retorna o valor e o banco de dados
            return x2, newton_db
        
        # Atualiza o valor de x1 para o próximo loop
        x1 = x2
    
    # Se o método não convergir dentro do número máximo de iterações, retorna o último valor calculado e o banco de dados
    return x1, newton_db
