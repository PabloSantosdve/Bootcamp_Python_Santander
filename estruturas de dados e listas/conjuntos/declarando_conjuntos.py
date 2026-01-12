# Criando um conjunto (set) a partir de uma lista com números repetidos
# Conjuntos removem automaticamente os elementos duplicados
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # Saída: {1, 2, 3, 4}

# Criando um conjunto a partir de uma string
# Cada letra vira um item no conjunto e letras repetidas são eliminadas
letras = set("abacaxi")
print(letras)  # Saída: {'b', 'a', 'c', 'x', 'i'} (ordem pode variar)

# Criando um conjunto a partir de uma tupla com nomes de carros
# A palavra "palio" aparece duas vezes, mas só uma é mantida no conjunto
carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # Saída: {'gol', 'celta', 'palio'} (ordem pode variar)


linguagens = {"Python", "Java", "Python", "SQL"}
print(linguagens)