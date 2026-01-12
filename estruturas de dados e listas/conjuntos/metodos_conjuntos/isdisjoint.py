# Criando três conjuntos com diferentes elementos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# O método isdisjoint() verifica se dois conjuntos são *disjuntos*,
# ou seja, se eles NÃO compartilham nenhum elemento em comum.
# Ele retorna True se os conjuntos forem completamente distintos (sem interseção),
# e False se houver pelo menos um elemento igual entre eles.

# Neste exemplo, conjunto_a e conjunto_b não têm nenhum número em comum.
# Portanto, eles são disjuntos, e o resultado será True.
resultado = conjunto_a.isdisjoint(conjunto_b)
print(resultado)  # Saída: True

# Já neste caso, conjunto_a e conjunto_c compartilham o número 1.
# Como existe um elemento em comum, eles NÃO são disjuntos.
# Por isso, o resultado será False.
resultado = conjunto_a.isdisjoint(conjunto_c)
print(resultado)  # Saída: False

