# Acesso direto a elementos de uma lista em Python
# Listas permitem acesso direto aos seus elementos através de índices.# O índice começa em 0, então o primeiro elemento está no índice 0, o segundo no índice 1, e assim por diante.
# Você pode acessar um elemento específico da lista usando a sintaxe lista[indice]. Por exemplo, para acessar o primeiro elemento de uma lista chamada frutas, você usaria frutas[0].

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã
print(frutas[2])  # uva

# Você também pode acessar elementos a partir do final da lista usando índices negativos. Por exemplo, frutas[-1] acessa o último elemento da lista, frutas[-2] acessa o penúltimo elemento, e assim por diante.
print(frutas[-1])  # pera   
print(frutas[-2])  # uva
# Se você tentar acessar um índice que está fora do intervalo da lista, Python levantará um erro IndexError.
# Por exemplo, se você tentar acessar frutas[4] em uma lista com apenas 4 elementos, você receberá um erro.
# print(frutas[4])  # Isso causará um erro IndexError