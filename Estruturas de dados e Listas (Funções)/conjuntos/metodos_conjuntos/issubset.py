# Criando dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# O método issubset() verifica se todos os elementos de conjunto_a estão presentes em conjunto_b.
# Neste caso, os elementos 1, 2 e 3 (de conjunto_a) também estão em conjunto_b.
# Portanto, conjunto_a é um subconjunto de conjunto_b, e o resultado será True.
resultado = conjunto_a.issubset(conjunto_b)
print(resultado)  # Saída: True

# Agora verificamos o contrário: se conjunto_b é um subconjunto de conjunto_a.
# Como conjunto_b contém elementos extras (4, 5 e 6) que não estão em conjunto_a,
# ele NÃO está totalmente contido em conjunto_a. Por isso, o resultado será False.
resultado = conjunto_b.issubset(conjunto_a)
print(resultado)  # Saída: False
