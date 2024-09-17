import tkinter as tk
from tkinter import messagebox

def calculaTotal():
    preco = float(entryPreco.get())
    quantidade = float(entryQuantidade.get())
    total = preco * quantidade
    labelValorTotal.config(text=f"R$ {total:.2f}")

janela = tk.Tk()
janela.title("Faça o seu pedido:")

# ***** Pedido do lanche *****
labelLanche = tk.Label(janela,text="Lanche")
labelLanche.pack(padx=50, pady=5)

entryLanche = tk.Entry(janela, width=100)
entryLanche.pack(padx=50, pady=5)

# ***** A quantidade de lanches *****
labelQuantidade = tk.Label(janela,text="Quantidade")
labelQuantidade.pack(padx=50, pady=5)

entryQuantidade = tk.Entry(janela, width=100)
entryQuantidade.pack(padx=50, pady=5)

# ***** Preço do lanche *****
labelPreco = tk.Label(janela,text="Preço")
labelPreco.pack(padx=50, pady=5)

entryPreco = tk.Entry(janela, width=100)
entryPreco.pack(padx=50, pady=5)

# ***** Toltal do pedido *****

labelTotal = tk.Label(janela,text="Total do pedido")
labelTotal.pack(padx=50, pady=5)

labelValorTotal = tk.Label(janela, width=100)
labelValorTotal.pack(padx=50, pady=5)
                     
button_salvar = tk.Button(janela, text="Calcular total",command=calculaTotal)
button_salvar.pack(pady=20)

janela.geometry("400x400")

janela.mainloop()