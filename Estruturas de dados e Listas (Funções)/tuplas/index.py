# O método .index(valor) retorna o índice da primeira ocorrência do valor na tupla.
# Se o valor não existir, ele gera um erro (ValueError).

linguagens = ("python", "js", "c", "java", "csharp",)

# Encontra o índice da primeira ocorrência de "java" (índice 3)
print(linguagens.index("java"))  # Saída: 3

# Encontra o índice da primeira ocorrência de "python" (índice 0)
print(linguagens.index("python"))  # Saída: 0
