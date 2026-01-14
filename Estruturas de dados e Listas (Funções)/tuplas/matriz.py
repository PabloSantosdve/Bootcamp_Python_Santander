# Aqui temos uma tupla que contém outras tuplas — uma estrutura semelhante a uma matriz 3x3.
# Podemos acessar os elementos usando dois índices: o primeiro para a linha, o segundo para a coluna.

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Imprime a primeira linha (tupla) da matriz.
print(matriz[0])  # Saída: (1, "a", 2)

# Acessa o primeiro elemento da primeira linha: 1
print(matriz[0][0])  # Saída: 1

# Acessa o último elemento da primeira linha usando índice negativo: 2
print(matriz[0][-1])  # Saída: 2 

# Acessa o último elemento da última linha usando índices negativos: "c"
print(matriz[-1][-1])  # Saída: "c"
