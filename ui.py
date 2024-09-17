import tkinter as tk
from tkinter import simpledialog, messagebox

# Configuração básica da interface gráfica
root = tk.Tk()
root.withdraw()  # Esconde a janela principal

# Exemplo de uso
messagebox.showinfo("Boas vindas!", "Olá, mundo!")
nomeDigitado = simpledialog.askstring("Identificação","Qual é o seu nome?")
messagebox.showinfo("Tchau",f"Seu nome é {nomeDigitado}")