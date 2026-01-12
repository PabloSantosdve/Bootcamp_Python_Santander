# Criando dois conjuntos com alguns elementos em comum e outros diferentes
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# O método symmetric_difference() retorna um novo conjunto com os elementos que estão em um conjunto OU no outro,
# mas NÃO em ambos. Ou seja, ele exclui os elementos que são comuns aos dois conjuntos.

# Neste exemplo, os elementos 2 e 3 são comuns, então são excluídos do resultado.

# O resultado será {1, 4}, que são os elementos exclusivos de cada conjunto.
resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)  # Saída: {1, 4}

# Também é possível usar o operador ^ (circunflexo) para fazer a diferença simétrica
print(conjunto_a ^ conjunto_b)  # Saída: {1, 4}
