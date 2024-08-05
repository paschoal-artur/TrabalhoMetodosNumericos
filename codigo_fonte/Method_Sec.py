# Importando funções auxiliares do módulo `func_main`
from func_main import f, insert_db

# Função que implementa o método da Secante
def secante(C, x0, x1, err1, err2, max_iter):
    ''' Parameters
    C: Constante utilizada na função `f`
    x0: Primeiro chute inicial
    x1: Segundo chute inicial
    err1: Tolerância para o erro absoluto da função
    err2: Tolerância para a diferença entre chutes consecutivos
    max_iter: Número máximo de iterações permitidas
    '''
    # Inicializa um dicionário para armazenar os resultados do método
    sec_db = {
        'k': [],         # Iterações
        'Q0': [],        # Valor atual de Q (antes da iteração)
        'Q1': [],        # Valor próximo de Q (após a iteração)
        'Custo': [],     # Custo da iteração
        'Erro': []       # Erro da iteração
    }

    # Contador para as iterações
    k = 0
    
    # Verifica se o primeiro chute x0 está suficientemente próximo da raiz
    if abs(f(x0, C)) < err1:
        # Se sim, insere o resultado no banco de dados e retorna x0
        insert_db(C, k, x0, x1, sec_db)
        return x0, sec_db
    
    # Verifica se o segundo chute x1 está suficientemente próximo da raiz
    # ou se a diferença entre x1 e x0 é menor que o erro permitido
    if abs(f(x1, C)) < err1 or abs(x1 - x0) < err2:
        # Se sim, insere o resultado no banco de dados e retorna x1
        insert_db(C, k, x0, x1, sec_db)
        return x1, sec_db
    
    # Loop para executar o método da Secante até o número máximo de iterações
    while k < max_iter:
        # Calcula o próximo valor de x usando a fórmula da Secante
        x2 = x1 - (f(x1, C) * (x1 - x0)) / (f(x1, C) - f(x0, C))
        
        # Insere os resultados da iteração no banco de dados
        insert_db(C, k, x1, x2, sec_db)
        
        # Verifica se o novo valor x2 atende ao critério de convergência
        # Se f(x2) está menor que o erro permitido ou a diferença entre x2 e x1 é menor que o erro permitido
        if abs(f(x2, C)) < err1 or abs(x2 - x1) < err2:
            # Se sim, retorna o valor x2 e o banco de dados
            return x2, sec_db
        
        # Atualiza x0 e x1 para a próxima iteração
        x0, x1 = x1, x2
        
        # Incrementa o contador de iterações
        k += 1
    
    # Se o método não convergir dentro do número máximo de iterações, retorna o último valor calculado e o banco de dados
    return x2, sec_db

# Função para análise de sinais, utilizada para encontrar intervalos onde a função muda de sinal
def analise_sinais(C, a, int_max=100):
    ''' Parameters
    C: Constante utilizada na função `f`
    a: Primeiro chute inicial
    int_max: Número máximo de iterações para tentar encontrar um intervalo
    '''
    # Define b como um valor próximo a a
    b = -1*a
    k = 0
    # Enquanto a função f(a) e f(b) tiverem o mesmo sinal
    while (f(a, C) * f(b, C)) > 0:
        # Verifica se o número máximo de iterações foi alcançado
        if k > int_max:
            # Se sim, imprime uma mensagem de erro e retorna
            return print('Error')
        # Calcula um novo ponto d para tentar encontrar uma mudança de sinal
        d = (a * f(b, C) - b * f(a, C)) / (f(b, C) - f(a, C))
        # Atualiza os pontos a e b com base no sinal da função em d
        if (f(a, C) * f(d, C)) > 0:
            a = d
        else:
            b = d
        # Incrementa o contador de iterações
        k += 1
    # Retorna o ponto b onde a mudança de sinal foi detectada
    return b
