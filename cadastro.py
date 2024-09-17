import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro do cliente")

# ***** Cadastro do nome do cliente *****
labelNome = tk.Label(janela,text="Nome")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela, width=100)
entryNome.pack(padx=50, pady=5)

# ***** Cadastro do telefone do ciente *****
labelTelefone = tk.Label(janela,text="Telefone")
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela, width=100)
entryTelefone.pack(padx=50, pady=5)

# ***** Cadastro do email do cliente *****
labelEmail = tk.Label(janela,text="Email")
labelEmail.pack(padx=50, pady=5)

entryEmail = tk.Entry(janela, width=100)
entryEmail.pack(padx=50, pady=5)

buttonSalvar = tk.Button(janela,text="Salvar", command=mensagem)
buttonSalvar.pack(padx=50, pady=5)

janela.geometry("400x300")

janela.mainloop()