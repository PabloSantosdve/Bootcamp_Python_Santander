# Criando um conjunto com números, incluindo valores repetidos
# Conjuntos em Python automaticamente eliminam duplicatas.
# Mesmo que você tente adicionar o mesmo número várias vezes, ele aparecerá apenas uma vez.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)  # Saída: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# O método discard() remove um elemento do conjunto, se ele existir.
# Se o elemento estiver presente, ele será removido.
numeros.discard(1)  # Remove o número 1 do conjunto

# Tentativa de remover o número 45, que não existe no conjunto.
# O método discard() NÃO gera erro nesse caso — ele simplesmente ignora a operação.
numeros.discard(45)

# O conjunto atualizado, sem o número 1
print(numeros)  # Saída: {0, 2, 3, 4, 5, 6, 7, 8, 9}
