# Criando dois conjuntos com alguns elementos em comum e alguns diferentes
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# O método difference() retorna um novo conjunto com os elementos que estão em conjunto_a,
# mas que NÃO estão em conjunto_b. Ou seja, ele subtrai os elementos de conjunto_b de conjunto_a.
resultado = conjunto_a.difference(conjunto_b)
print(resultado)  # Saída: {1} — porque 1 está apenas em conjunto_a

# Agora faz o contrário: retorna os elementos que estão em conjunto_b, mas não em conjunto_a
resultado = conjunto_b.difference(conjunto_a)
print(resultado)  # Saída: {4} — porque 4 está apenas em conjunto_b

# Também é possível usar o operador - (hífen) para fazer a diferença entre conjuntos
print(conjunto_a - conjunto_b)  # Saída: {1}
print(conjunto_b - conjunto_a)  # Saída: {4}
