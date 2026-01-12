# Criando um conjunto com dois elementos
sorteio = {1, 23}
print(sorteio)  # Saída: {1, 23}

# O método clear() remove TODOS os elementos do conjunto.
# Ele não deleta o conjunto em si, apenas o esvazia.
# Após essa operação, o conjunto ainda existe, mas está vazio.
sorteio.clear()

# Agora o conjunto está vazio.
# A saída será set(), que é a forma como Python representa um conjunto vazio.
print(sorteio)  # Saída: set()
