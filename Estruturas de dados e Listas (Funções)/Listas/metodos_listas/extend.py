# O método .extend() é usado para adicionar vários elementos (de outra lista)
# ao final da lista original. Ele "expande" a lista, inserindo os itens individualmente.
# Diferente do .append(), que adiciona a lista inteira como um único item.

# Criamos uma lista chamada 'linguagens' com três elementos.
linguagens = ["python", "js", "c"]

# Exibimos a lista original.
print(linguagens)  # Saída: ["python", "js", "c"]

# Adicionamos duas novas linguagens usando .extend().
linguagens.extend(["java", "csharp"])

# Exibimos a lista após a extensão.
print(linguagens)  # Saída: ["python", "js", "c", "java", "csharp"]
