# Tuplas podem ser percorridas (iteradas) com loops for para acessar seus elementos.
# O loop 'for carro in carros' percorre cada elemento da tupla e imprime o valor.

carros = (
    "gol",
    "celta",
    "palio",
)

# Imprime cada carro da tupla em linhas separadas.
for carro in carros:
    print(carro)

# A função enumerate() retorna pares (índice, valor) ao iterar.
# Isso permite acessar o índice do elemento junto com seu valor.

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")  # Exemplo de saída: "0: gol"
