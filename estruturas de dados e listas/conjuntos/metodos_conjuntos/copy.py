# Criando um conjunto com dois elementos
sorteio = {1, 23}
print(sorteio)  # Saída: {1, 23}

# O método copy() cria uma **cópia independente** do conjunto original.
# No entanto, neste exemplo, a cópia foi criada mas **não foi armazenada em nenhuma variável**,
# então ela é imediatamente descartada e não pode ser usada depois.
sorteio.copy()

# O conjunto original permanece inalterado
print(sorteio)  # Saída: {1, 23}
