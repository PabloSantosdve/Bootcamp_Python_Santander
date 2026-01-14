# O método .index(valor) retorna o índice da primeira ocorrência do valor na lista.
# Se o valor não existir na lista, ele gera um erro (ValueError).
# É útil para saber em que posição um elemento está dentro da lista.

# Criamos uma lista chamada 'linguagens' com várias linguagens de programação.
linguagens = ["python", "js", "c", "java", "csharp"]

# Imprime o índice onde "java" está na lista. Saída: 3
print(linguagens.index("java"))

# Imprime o índice onde "python" está na lista. Saída: 0
print(linguagens.index("python"))
