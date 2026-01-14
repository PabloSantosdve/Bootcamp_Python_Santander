# Criando dois conjuntos com alguns elementos em comum e alguns diferentes
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# O método intersection() retorna um novo conjunto contendo apenas os elementos que estão presentes em ambos os conjuntos.
# Ou seja, ele identifica a interseção entre os conjuntos.
# Neste exemplo, os elementos 2 e 3 estão presentes tanto em conjunto_a quanto em conjunto_b.
resultado = conjunto_a.intersection(conjunto_b)
print(resultado)  # Saída: {2, 3}

# Outros exemplos:
conjunto_c = {5, 6, 7}
conjunto_d = {7, 8, 9}
print(conjunto_c.intersection(conjunto_d))  # Saída: {7}

# Também é possível usar o operador & (E comercial) para fazer a interseção
print(conjunto_a & conjunto_b)  # Saída: {2, 3}
