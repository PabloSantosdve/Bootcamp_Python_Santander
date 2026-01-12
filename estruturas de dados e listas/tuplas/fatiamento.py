# O fatiamento (slicing) permite extrair partes da tupla usando a sintaxe:
# tupla[início:fim:passo]
# - início: índice inicial (inclusivo)
# - fim: índice final (exclusivo)
# - passo: intervalo entre os elementos selecionados (padrão é 1)
# Índices negativos e omissões são permitidos para flexibilidade.

tupla = ("p", "y", "t", "h", "o", "n",)

# Elementos a partir do índice 2 até o fim: ("t", "h", "o", "n")
print(tupla[2:])  

# Elementos do início até antes do índice 2: ("p", "y")
print(tupla[:2])  

# Elementos do índice 1 até antes do índice 3: ("y", "t")
print(tupla[1:3])  

# Elementos do índice 0 até antes do índice 3, pulando de 2 em 2: ("p", "t")
print(tupla[0:3:2])  

# Todos os elementos (equivalente a copiar a tupla): ("p", "y", "t", "h", "o", "n")
print(tupla[::])  

# Todos os elementos em ordem inversa (passo -1): ("n", "o", "h", "t", "y", "p")
print(tupla[::-1])  
