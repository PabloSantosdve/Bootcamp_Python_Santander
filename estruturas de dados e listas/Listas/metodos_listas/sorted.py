# A função sorted() retorna uma NOVA lista ordenada, sem alterar a lista original.
# É diferente do método .sort(), que modifica a lista diretamente.
# Podemos usar os mesmos argumentos: key= para personalizar a ordenação, e reverse=True para inverter.

# Aqui usamos lambda x: len(x) como chave de ordenação.
# Isso significa que os itens serão ordenados pelo tamanho (comprimento) de cada string.

linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena os itens do menor para o maior, com base no tamanho (número de caracteres)
print(sorted(linguagens, key=lambda x: len(x)))  
# Saída: ["c", "js", "java", "python", "csharp"]

# Agora usamos reverse=True para inverter a ordem: do maior para o menor
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  
# Saída: ["python", "csharp", "java", "js", "c"]

# Observação:
# A lista original 'linguagens' continua a mesma, pois sorted() não a modifica.
