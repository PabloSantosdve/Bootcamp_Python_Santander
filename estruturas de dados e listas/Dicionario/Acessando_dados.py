# Criamos um dicionário chamado 'dados' com três pares chave-valor:
# "nome" associado a "Guilherme", "idade" associado a 28, e "telefone" associado a "3333-1234"
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Acessamos os valores do dicionário usando suas chaves:
dados["nome"]      # Retorna "Guilherme"
dados["idade"]     # Retorna 28
dados["telefone"]  # Retorna "3333-1234"

# Agora, atualizamos os valores associados às chaves existentes:
dados["nome"] = "Maria"         # Altera o valor da chave "nome" para "Maria"
dados["idade"] = 18             # Altera o valor da chave "idade" para 18
dados["telefone"] = "9988-1781" # Altera o valor da chave "telefone" para "9988-1781"

# O dicionário agora está assim:
# {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
dados
