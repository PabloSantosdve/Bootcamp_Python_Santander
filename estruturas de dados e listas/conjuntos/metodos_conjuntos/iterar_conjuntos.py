# Criando um conjunto com nomes de carros
carros = {"gol", "celta", "palio"}

# Iterando sobre o conjunto e imprimindo cada carro
# Como conjuntos não têm ordem fixa, a ordem da impressão pode variar
for carro in carros:
    print(carro[0])

# Iterando sobre o conjunto com a função enumerate()
# Essa função gera um índice para cada elemento junto com o próprio elemento
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
