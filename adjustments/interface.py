import tkinter as tk
from tkinter import *
from tkinter import ttk
from app import *
# Cria a janela principal
janela1 = tk.Tk()
janela1.title("Quadro resposta")

# Cria o notebook (contêiner de abas)
notebook = ttk.Notebook(janela1)

# Cria frames para cada aba
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
aba3 = ttk.Frame(notebook)

# Adiciona as abas ao notebook
notebook.add(aba1, text="Ponto Fixo")
notebook.add(aba2, text="Newton Modificado")
notebook.add(aba3, text="Secante Original")

# Empacota o notebook na janela principal
notebook.pack(expand=1, fill="both")

# Adiciona widgets a cada aba
columns_fix = ['k', 'Q0', 'Q1', 'Custo', 'Erro']

label1 = ttk.Treeview(aba1, selectmode='browse', columns=columns_fix, show='headings')
label1.pack(pady=10, padx=10)

label2 = ttk.Treeview(aba2, selectmode='browse', columns=columns_fix, show='headings')
label2.pack(pady=10, padx=10)

label3 = ttk.Treeview(aba3, selectmode='browse', columns=columns_fix, show='headings')
label3.pack(pady=10, padx=10)

# Insere dados na Treeview
def construct(label, db):
    label.column('k', width=20, minwidth=10, stretch=NO)
    label.heading('#1', text='k')

    label.column('Q0', width=100, minwidth=50, stretch=NO)
    label.heading('#2', text='Q0')

    label.column('Q1', width=100, minwidth=50, stretch=NO)
    label.heading('#3', text='Q1')

    label.column('Custo', width=100, minwidth=50, stretch=NO)
    label.heading('#4', text='Custo')

    label.column('Erro', width=100, minwidth=50, stretch=NO)
    label.heading('#5', text='Erro')

    # Insere os elementos do banco de dados na aba 
    elementos = []
    for i in range(0, len(db['k'])):
        for key, value in db.items():
            elementos.append(db[key][i])
        label.insert("", END, values=elementos, tag=i)
        elementos = []

# Carrega os dados de cada banco de dados
construct(label1, sec_db)
construct(label2, newton_db)
construct(label3, mpf_db)

# Inicia a interface
janela1.mainloop()