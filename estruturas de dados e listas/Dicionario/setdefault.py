contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# .setdefault(chave, valor_padrao) faz o seguinte:
# - Se a chave EXISTIR, retorna o valor atual dela (sem mudar nada)
# - Se a chave NÃO EXISTIR, adiciona a chave com o valor padrão que você passar e retorna esse valor

# Aqui a chave "nome" já existe, então retorna o valor atual e NÃO muda nada
contato.setdefault("nome", "Giovanna")  # retorna "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# Aqui a chave "idade" NÃO existe, então adiciona ela com valor 28
# E retorna 28
contato.setdefault("idade", 28)  # retorna 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
