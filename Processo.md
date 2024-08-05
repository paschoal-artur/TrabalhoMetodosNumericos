# `Método do Ponto Fixo`
## Parâmetros Utilizados no Método:
1. Função Definida para o Método:
- `Q`: Valor Atual
- `C`: Constante utilizada na função `f`
2. Função Principal: 
- `C`: Constante utilizada na função `f` e sua derivada `df`
- `x0`: Chute inicial para o valor de `Q`
- `err`: Tolerância para a convergência
- `max_iter`: Número máximo de iterações permitidas
## Passo a Passo do Algoritmo:
1. Definimos a função `phi(Q)`
    - Limitamos o domínio para evitar `overflow`
    - Garantimos a positividade do valor
    - Retorna NaN em caso de `overflow`
2. Verificamos se o valor inicial `x0` já está próximo do zero (dentro do erro tolerável)
3. Iniciamos o loop para as iterações do método do ponto fixo
    - Calculamos o próximo valor de `x` usando a função `phi`
    - Verificamos se o novo valor de `x` está suficientemente próximo do zero (dentro do erro tolerável)
4. Retornamos os valores finais

# `Newton Raphson Modificado`
## Parâmetros utilizados no Método:
1. Derivada da Função
- `Q`: Valor atual de `Q`
- `C`: Constante utilizada na função `f`
2. Função principal
- `C`: Constante utilizada na função `f`
- `x0`: Primeiro chute inicial
- `err1`: Tolerância para o erro absoluto da função
- `max_iter`: Número máximo de iterações permitidas
## Passo a Passo do Algoritmo:
1. Define o chute inicial `x0` como o valor atual `x1`
    - Verifica se o chute inicial `x0` já está suficientemente perto de zero
    - Se já estiver perto de zero retorna o valor
2. Loop para realizar o método de Newton modificado até o número máximo de iterações
    -  Calcula o próximo valor de `Q` usando o método de Newton
    -  Verifica se a solução está dentro do erro permitido ou se a mudança é pequena o suficiente
    -  Se a solução for aceitável, retorna o valor
    -  Atualiza o valor de `x1` para o próximo loop
3. Se o método não convergir dentro do número máximo de iterações, retorna o último valor calculado

# `Método da Secante`
## Parâmetros Utilizados no Método: 
1. Função principal
- `C`: Constante utilizada na função `f`
- ``x0``: Primeiro chute inicial
- ``x1``: Segundo chute inicial
- `err1`: Tolerância para o erro absoluto da função
- `err2`: Tolerância para a diferença entre chutes consecutivos
- `max_iter`: Número máximo de iterações permitidas

2. Segunda função (analise sinais)
- `C`: Constante utilizada na função `f`
- `a`: Primeiro chute inicial
- `int_max`: Número máximo de iterações para tentar encontrar um intervalo
## Passo a Passo do Algoritmo:
1. Contador para as iterações
2. Verificamos se o primeiro chute ``x0`` está suficientemente próximo da raiz, se sim retorna ``x0``
3. Verificamos se o segundo chute `x1` está suficientemente próximo da raiz
    - Ou se a diferença de `x1` e `x0` é menor que o erro permitido, se sim insere o resultado e retorna `x1`
4. Loop para executar o método da secante até o `max itter`
    - Calculamos o próximo valor de `x` usando a fórmula da secante
    - Verificamos se o novo valor `x2` atende ao critério de convergência
    - Se `f(x2)` está menor que o erro permitido ou a diferença entre `x2` e `x1` é menor que o erro permitido, se sim retorna `x2`
    - Atualizamos `x0` e `x1` para a próxima iteração
    - Incrementa o contador
5. Se o método não convergir dentro do número máximo de iterações, retorna o último valor calculado 
6. Função para análise de sinais, utilizada para encontrar intervalos onde a função muda de sinal
    - Define `b` como um valor próximo à `a`
    - Enquanto a função `f(a)` e `f(b)` tiverem o mesmo sinal, verifica se o número máximo de iterações foi alcançado
    - Calcula um novo ponto `d` para tentar encontrar uma mudança de sinal
    - Atualiza os pontos `a` e `b` com base no sinal da função em `d`
    - Incrementa o contador de iterações
    - Retorna o ponto `b` onde a mudança de sinal foi detectada

# Comparação Para Diferentes Custos 
1. Listamos diferentes valores e depois calculamos um loop para iterar sobre os diferentes valores
2. Na outra célula nós plotamos uma tabela e gráficos de comparações para os diferentes valores de C