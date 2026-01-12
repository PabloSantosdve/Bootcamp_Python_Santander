# Criando dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# O método issuperset() verifica se conjunto_a contém TODOS os elementos de conjunto_b.
# Neste caso, conjunto_a NÃO contém todos os elementos de conjunto_b (faltam 4, 5 e 6),
# então o resultado será False.
resultado = conjunto_a.issuperset(conjunto_b)
print(resultado)  # Saída: False

# Agora verificamos se conjunto_b contém todos os elementos de conjunto_a.
# Como conjunto_b tem os elementos 1, 2 e 3 (que são todos os elementos de conjunto_a),
# então conjunto_b é um superconjunto de conjunto_a, e o resultado será True.
resultado = conjunto_b.issuperset(conjunto_a)
print(resultado)  # Saída: True
