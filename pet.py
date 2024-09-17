import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro pet shop")

# ***** Cadastro do nome do tutor do pet *****
labelNome = tk.Label(janela,text="Nome do tutor do pet")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela, width=100)
entryNome.pack(padx=50, pady=5)

# ***** Cadastro do nome do pet *****
labelNomepet = tk.Label(janela,text="Nome do Pet")
labelNomepet.pack(padx=50, pady=5)

entryNomepet = tk.Entry(janela, width=100)
entryNomepet.pack(padx=50, pady=5)

# ***** Cadastro da data de nascimento do pet *****
labelNascimentopet = tk.Label(janela,text="Data de nascimento do Pet")
labelNascimentopet.pack(padx=50, pady=5)

entryNascimentopet = tk.Entry(janela, width=100)
entryNascimentopet.pack(padx=50, pady=5)

# ***** Cadastro espécie do pet *****

labelEspeciepet = tk.Label(janela,text="Especie do Pet")
labelEspeciepet.pack(padx=50, pady=5)

entryEspeciepet = tk.Entry(janela, width=100)
entryEspeciepet.pack(padx=50, pady=5)

# ***** Cadastro Raça do pet *****

labelRacapet = tk.Label(janela,text="Raça do pet")
labelRacapet.pack(padx=50, pady=5)

entryRacapet = tk.Entry(janela, width=100)
entryRacapet.pack(padx=50, pady=5)

button_salvar = tk.Button(janela, text="Salvar")
button_salvar.pack(pady=20)

janela.geometry("400x400")

janela.mainloop()

# ***** Combo
lista = {'Cachorro','Gato','Tomagochi'}
tupla = ("Macaco","Leão","Elefante")
comboboxEspecie = ttk.Combobox(janela)
comboboxEspecie.pack(padx=10, pady=5)