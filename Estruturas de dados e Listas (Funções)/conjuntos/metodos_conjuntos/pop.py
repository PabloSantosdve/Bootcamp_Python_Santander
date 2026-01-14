# Criando um conjunto com números, duplicatas serão removidas automaticamente
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Imprime o conjunto completo
# A ordem dos elementos pode variar, pois conjuntos (sets) não mantêm ordem
print(numeros)  # Exemplo de saída: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# O método pop() remove e retorna um elemento "aleatório" do conjunto.
# Na prática, ele geralmente remove o primeiro elemento da ordem interna do set,
# mas como conjuntos não têm ordem definida, o elemento removido pode variar.
print(numeros.pop())  # Exemplo: 0

# Remove e retorna outro elemento do conjunto
print(numeros.pop())  # Exemplo: 1

# Imprime o conjunto após duas remoções
print(numeros)  # Exemplo de saída: {2, 3, 4, 5, 6, 7, 8, 9}
