# Tuplas são sequências ordenadas e imutáveis.
# Usando índices negativos, podemos acessar elementos a partir do final:
# índice -1 é o último elemento, -2 é o penúltimo, etc.

frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

# Acessa o último elemento da tupla, que é "pera"
print(frutas[-1])  # Saída: pera

# Acessa o terceiro elemento a partir do final, que é "laranja"
print(frutas[-3])  # Saída: laranja
