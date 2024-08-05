# Importando as bibliotecas necessárias
import numpy as np
from func_main import f, insert_db

# Definindo a função phi(Q) usada no método do ponto fixo
def phi(Q, C):
    ''' Parameters
    Q: Valor atual de Q
    C: Constante utilizada na função `f`
    '''
    # A função retorna a raiz quadrada do produto de C e a exponencial de Q dividida por 4
    return np.sqrt((C * np.exp(Q)) / 4)

# Implementando o método do ponto fixo
def ponto_fixo(C, x0, err, max_iter=100):
    ''' Parameters
    C: Constante utilizada na função `f` e sua derivada `df`
    x0: Chute inicial para o valor de Q
    err: Tolerância para a convergência
    max_iter: Número máximo de iterações permitidas
    '''
    # Inicializando um dicionário para armazenar os resultados do método do ponto fixo
    mpf_db = {
        'k': [],         # Iterações
        'Q0': [],        # Valor atual de Q (antes da iteração)
        'Q1': [],        # Valor próximo de Q (após a iteração)
        'Custo': [],     # Custo da iteração
        'Erro': []       # Erro da iteração
    }
    
    # Inicializando x1 com o valor inicial x0
    x1 = x0
    
    # Verificando se o valor inicial x0 já está próximo do zero (dentro do erro tolerável)
    if abs(f(x0, C)) < err:
        # Inserindo os dados da iteração 0 no banco de dados
        insert_db(C, 0, x0, x1, mpf_db)
        # Retornando o valor inicial x0 e o banco de dados
        return x0, mpf_db
    
    # Iniciando o loop para as iterações do método do ponto fixo
    for i in range(max_iter):
        # Calculando o próximo valor de x usando a função phi
        x2 = phi(x1, C)
        
        # Inserindo os dados da iteração atual no banco de dados
        insert_db(C, i, x1, x2, mpf_db)
        
        # Verificando se o novo valor de x está suficientemente próximo do zero (dentro do erro tolerável)
        # ou se a diferença entre os valores sucessivos de x é menor que o erro tolerável
        if abs(f(x2, C)) < err or abs(x2 - x1) < err:
            # Retornando o valor final x2 e o banco de dados
            return x2, mpf_db
        
        # Atualizando x1 com o valor de x2 para a próxima iteração
        x1 = x2
    
    # Se o número máximo de iterações for atingido, retornando o valor atual de x1 e o banco de dados
    return x1, mpf_db
