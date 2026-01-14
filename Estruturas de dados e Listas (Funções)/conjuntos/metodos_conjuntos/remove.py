# Criando um conjunto com números (elementos duplicados são removidos automaticamente)
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Imprime o conjunto original
print(numeros)  # Saída: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# O método remove() remove o elemento especificado do conjunto.
# Se o elemento estiver presente, ele será removido.
# IMPORTANTE: se o elemento NÃO existir, o método gera um erro (KeyError).
# Além disso, remove() não retorna o valor removido — ele retorna None.
print(numeros.remove(0))  # Remove o número 0, mas imprime None

# Imprime o conjunto após remover o elemento 0
print(numeros)  # Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9}
