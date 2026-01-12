# Criando um conjunto com dois números
sorteio = {1, 23}

# O método add() serve para adicionar um novo elemento ao conjunto.
# Se o elemento ainda não estiver presente, ele será adicionado normalmente.
sorteio.add(25)  # Adiciona o número 25 ao conjunto
print(sorteio)   # Saída: {1, 23, 25}

# Adicionando mais um número ao conjunto
sorteio.add(42)  # Adiciona o número 42
print(sorteio)   # Saída: {1, 23, 25, 42}

# Tentando adicionar um número que já está no conjunto
# Como conjuntos não permitem elementos duplicados, nada acontece.
# Nenhum erro é gerado, mas o conjunto permanece igual.
sorteio.add(25)  # 25 já está presente, então não é adicionado novamente
print(sorteio)   # Saída: {1, 23, 25, 42}
