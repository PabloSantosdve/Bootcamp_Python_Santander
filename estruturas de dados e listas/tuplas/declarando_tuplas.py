# Em Python, tuplas são coleções ordenadas e imutáveis (não podem ser alteradas após a criação).
# Elas são definidas com parênteses () e podem conter qualquer tipo de dado.

# Criando uma tupla com 3 frutas
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)  # Saída: ('laranja', 'pera', 'uva')

# Criando uma tupla a partir de uma string.
# Cada letra da palavra "python" se torna um elemento da tupla.
letras = tuple("python")
print(letras)  # Saída: ('p', 'y', 't', 'h', 'o', 'n')

# Criando uma tupla a partir de uma lista.
numeros = tuple([1, 2, 3, 4])
print(numeros)  # Saída: (1, 2, 3, 4)

# Criando uma tupla com um único elemento.
# Importante: é necessário a vírgula no final para indicar que é uma tupla, não apenas um valor entre parênteses.
pais = ("Brasil",)
print(pais)  # Saída: ('Brasil',)
