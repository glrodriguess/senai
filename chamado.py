import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

# Função para carregar os dados dos chamados do arquivo JSON
def carregar_chamados():
    if os.path.exists('chamados.json'):
        with open('chamados.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

# Função para salvar os dados dos chamados no arquivo JSON
def salvar_chamados(chamados):
    with open('chamados.json', 'w') as arquivo:
        json.dump(chamados, arquivo, indent=4)

# Função para obter o próximo número de chamado
def obter_proximo_numero_chamado(chamados):
    if not chamados:
        return 1
    else:
        return max(chamado['numero_chamado'] for chamado in chamados) + 1

# Função para salvar um novo chamado
def salvar_chamado():
    nome_cliente = entrada_nome_cliente.get()
    tipo_problema = combo_tipo_problema.get()
    descricao_problema = texto_descricao_problema.get("1.0", tk.END).strip()
    prioridade = combo_prioridade.get()
    numero_chamado = int(rotulo_numero_chamado.cget("text"))
    data_abertura = rotulo_data_abertura.cget("text")

    # Validação dos campos
    if not nome_cliente or not tipo_problema or not descricao_problema or not prioridade:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
        return

    novo_chamado = {
        "numero_chamado": numero_chamado,
        "cliente": nome_cliente,
        "tipo_problema": tipo_problema,
        "descricao": descricao_problema,
        "prioridade": prioridade,
        "data_abertura": data_abertura
    }

    chamados = carregar_chamados()
    chamados.append(novo_chamado)
    salvar_chamados(chamados)

    messagebox.showinfo("Sucesso", "Chamado salvo com sucesso!")
    novo_chamado()

# Função para criar um novo chamado
def novo_chamado():
    entrada_nome_cliente.delete(0, tk.END)
    combo_tipo_problema.set('')
    texto_descricao_problema.delete("1.0", tk.END)
    combo_prioridade.set('')
    data_abertura = datetime.now().strftime("%Y-%m-%d")
    rotulo_data_abertura.config(text=data_abertura)
    
    chamados = carregar_chamados()
    proximo_numero_chamado = obter_proximo_numero_chamado(chamados)
    rotulo_numero_chamado.config(text=proximo_numero_chamado)

# Função para localizar um chamado
def localizar_chamado():
    numero_chamado_str = entrada_numero_pesquisa.get()
    
    # Validação do número do chamado
    if not numero_chamado_str.isdigit():
        messagebox.showwarning("Aviso", "Por favor, insira um número de chamado válido.")
        return
    
    numero_chamado = int(numero_chamado_str)
    chamados = carregar_chamados()
    
    for chamado in chamados:
        if chamado['numero_chamado'] == numero_chamado:
            entrada_nome_cliente.delete(0, tk.END)
            entrada_nome_cliente.insert(0, chamado['cliente'])
            combo_tipo_problema.set(chamado['tipo_problema'])
            texto_descricao_problema.delete("1.0", tk.END)
            texto_descricao_problema.insert("1.0", chamado['descricao'])
            combo_prioridade.set(chamado['prioridade'])
            rotulo_data_abertura.config(text=chamado['data_abertura'])
            rotulo_numero_chamado.config(text=chamado['numero_chamado'])
            return

    messagebox.showerror("Erro", "Chamado não encontrado.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sistema de Registro e Consulta de Chamados de Suporte Técnico")

# Layout dos campos
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Nome do Cliente:").grid(row=0, column=0, sticky=tk.W)
entrada_nome_cliente = tk.Entry(frame, width=40)
entrada_nome_cliente.grid(row=0, column=1)

tk.Label(frame, text="Tipo de Problema:").grid(row=1, column=0, sticky=tk.W)
combo_tipo_problema = ttk.Combobox(frame, values=["Problema de Rede", "Falha de Software", "Erro de Hardware"], width=37)
combo_tipo_problema.grid(row=1, column=1)

tk.Label(frame, text="Descrição do Problema:").grid(row=2, column=0, sticky=tk.NW)
texto_descricao_problema = tk.Text(frame, height=4, width=40)
texto_descricao_problema.grid(row=2, column=1)

tk.Label(frame, text="Prioridade:").grid(row=3, column=0, sticky=tk.W)
combo_prioridade = ttk.Combobox(frame, values=["Baixa", "Média", "Alta"], width=37)
combo_prioridade.grid(row=3, column=1)

tk.Label(frame, text="Data de Abertura:").grid(row=4, column=0, sticky=tk.W)
rotulo_data_abertura = tk.Label(frame, text=datetime.now().strftime("%Y-%m-%d"))
rotulo_data_abertura.grid(row=4, column=1)

tk.Label(frame, text="Número do Chamado:").grid(row=5, column=0, sticky=tk.W)
rotulo_numero_chamado = tk.Label(frame, text="1")
rotulo_numero_chamado.grid(row=5, column=1)

tk.Label(frame, text="Número do Chamado para Localizar:").grid(row=6, column=0, sticky=tk.W)
entrada_numero_pesquisa = tk.Entry(frame, width=40)
entrada_numero_pesquisa.grid(row=6, column=1)

# Botões
tk.Button(frame, text="Novo Chamado", command=novo_chamado).grid(row=7, column=0, pady=10)
tk.Button(frame, text="Localizar Chamado", command=localizar_chamado).grid(row=7, column=1, pady=10)
tk.Button(frame, text="Salvar Chamado", command=salvar_chamado).grid(row=7, column=2, pady=10)

# Inicializa o número do chamado
novo_chamado()

# Inicia o loop principal
root.mainloop()