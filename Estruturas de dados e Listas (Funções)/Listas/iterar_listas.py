# Iterar uma lista significa "passar por cada elemento da lista, um por um",
# para poder acessar, usar ou manipular esses elementos.

# Exemplo de lista
frutas = ['maçã', 'banana', 'laranja', 'uva']

# Usando um loop for para iterar a lista
for fruta in frutas:
    print(f'Eu gosto de {fruta}')




carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

