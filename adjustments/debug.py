# Exibir DataFrames
# print(f'from Method PF: {mpf_raiz}')
# print(df_mpf)
# print(f'\nFrom Method Newton: {newt_raiz}')
# print(df_newt)
# print(f'\nFrom Method Secante: {sec_raiz}')
# print(df_sec)

# Exportar para excel
# Usando ExcelWriter para criar um arquivo com múltiplas planilhas
# with pd.ExcelWriter('quadro_comparativo.xlsx', engine='openpyxl') as writer:
#     df_mpf.to_excel(writer, sheet_name='Ponto Fixo', index=False)
#     df_newt.to_excel(writer, sheet_name='Newton', index=False)
#     df_sec.to_excel(writer, sheet_name='Secante', index=False)


# # Tempo de execução
# import timeit
# from functools import partial
# mpf = partial(ponto_fixo, C, Q0)
# newt = partial(newton_mod, C, Q0)
# sec = partial(secante, Q0, Q1, err1, err1, max_iter=100)
# time_mpf = timeit.timeit(mpf, number=1)
# time_newt = timeit.timeit(newt, number=1)
# time_sec = timeit.timeit(sec, number=1)
# print(f"Tempo de execução mpf: {time_mpf} segundos\n")
# print(f"Tempo de execução newt: {time_newt} segundos\n")
# print(f"Tempo de execução sec: {time_sec} segundos\n")