from Method_PF import *
from Method_Newt import *
from Method_Sec import *
from func_main import *
import pandas as pd
import openpyxl

# Teste da função
C = 1
Q0 = 0.5
Q1 = analise_sinais(C, Q0)
err1 = 1e-4
raiz_mpf, mpf_db = ponto_fixo(C, Q0, err1)
raiz_newt, newton_db  = newton_mod(C, Q0, err1)
raiz_sec, sec_db = secante(C, Q0, Q1, err1, err1, max_iter=100)

df_mpf = pd.DataFrame(mpf_db)
df_newt = pd.DataFrame(newton_db)
df_sec = pd.DataFrame(sec_db)

# Exibir DataFrames

print(f'from Method PF: {raiz_mpf} ---> {viabilidade(raiz_mpf)}')
print(df_mpf)
print(f'\nFrom Method Newton: {raiz_newt}')
print(df_newt)
print(f'\nFrom Method Secante: {raiz_sec}')
print(df_sec)
