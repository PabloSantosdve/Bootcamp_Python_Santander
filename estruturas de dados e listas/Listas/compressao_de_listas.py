# Lista de números inteiros
numeros = [1, 30, 21, 2, 9, 65, 34]

# Filtrar apenas os números pares da lista.
# Usamos uma list comprehension com condição (if).
pares = [numero for numero in numeros if numero % 2 == 0]

# Exibe a lista contendo somente os números pares
print(pares)

# Redefinimos a lista original de números
numeros = [1, 30, 21, 2, 9, 65, 34]

# Criar uma nova lista com o quadrado de cada número da lista original.
# Também usamos list comprehension aqui, mas sem condição.
quadrado = [numero**2 for numero in numeros]

# Exibe a lista com os valores ao quadrado
print(quadrado)
