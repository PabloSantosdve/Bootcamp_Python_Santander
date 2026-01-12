# Criando um conjunto inicial
numeros = {10, 20}

# O método update() permite adicionar múltiplos elementos de uma vez ao conjunto.
# Ele pode receber qualquer estrutura iterável: listas, tuplas, outros conjuntos, etc.
numeros.update([30, 40, 50])  # Adiciona os elementos 30, 40 e 50
print(numeros)  # Saída: {10, 20, 30, 40, 50}

# Adicionando elementos de outro conjunto
outros = {60, 70}
numeros.update(outros)
print(numeros)  # Saída: {10, 20, 30, 40, 50, 60, 70}

# Se algum elemento já existir, ele não será duplicado (sem erro)
numeros.update([20, 80])
print(numeros)  # Saída: {10, 20, 30, 40, 50, 60, 70, 80}
