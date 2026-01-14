contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Verifica se a chave "guilherme@gmail.com" existe no dicionário contatos
resultado = "guilherme@gmail.com" in contatos  # True, porque existe
print(resultado)

# Verifica se a chave "megui@gmail.com" existe — não existe, então False
resultado = "megui@gmail.com" in contatos  
print(resultado)

# Verifica se a chave "idade" existe no dicionário interno do contato "guilherme@gmail.com"
# Não existe, então False
resultado = "idade" in contatos["guilherme@gmail.com"]  
print(resultado)

# Verifica se a chave "telefone" existe no contato "giovanna@gmail.com"
# Existe, então True
resultado = "telefone" in contatos["giovanna@gmail.com"]  
print(resultado)
