# Criando dois conjuntos com elementos diferentes
conjunto_a = {1, 2}
conjunto_b = {3, 4}

# O método union() retorna um novo conjunto contendo todos os elementos de ambos os conjuntos.
# Ele elimina automaticamente elementos duplicados, pois conjuntos não permitem duplicatas.
# Neste exemplo, o resultado será {1, 2, 3, 4}, que é a união dos elementos de conjunto_a e conjunto_b.
resultado = conjunto_a.union(conjunto_b)
print(resultado)  # Saída: {1, 2, 3, 4}

# Outros exemplos:
# União com elementos repetidos
conjunto_c = {1, 2, 3}
conjunto_d = {3, 4, 5}
print(conjunto_c.union(conjunto_d))  # Saída: {1, 2, 3, 4, 5}

# Também é possível usar o operador | (pipe) para fazer a união
print(conjunto_c | conjunto_d)  # Saída: {1, 2, 3, 4, 5}

