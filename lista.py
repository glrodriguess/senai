estoque = ["caneta","caderno","borracha","lapis"]

# Adicionar novo item no estoque
estoque.append("marcador")
print(estoque)

# Remover item do estoque
estoque.remove("lápis")
print(estoque)

# Verificar se um item esta em estoque
print("borracha" in estoque) # Saida: True