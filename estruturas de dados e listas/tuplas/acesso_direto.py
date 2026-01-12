# Tuplas são sequências ordenadas e imutáveis.
# Podemos acessar elementos usando índices positivos,
# onde o índice 0 é o primeiro elemento, 1 o segundo, e assim por diante.

frutas = ("maçã", "laranja", "uva", "pera",)

# Acessa o primeiro elemento da tupla: "maçã"
print(frutas[0])  # Saída: maçã

# Acessa o terceiro elemento da tupla: "uva"
print(frutas[2])  # Saída: uva

# Criando uma tupla com um único elemento
tupla1 = (42)       # Isso NÃO é uma tupla! É apenas um número inteiro entre parênteses
tupla2 = (42,)      # Isso SIM é uma tupla com um único elemento

print(type(tupla1))  # <class 'int'>
print(type(tupla2))  # <class 'tuple'>

# Criando uma tupla com múltiplos elementos e vírgula final
tupla3 = (
    "maçã",
    "banana",
    "laranja",
)  # A vírgula final aqui é OPCIONAL, mas recomendada

print(tupla3)
