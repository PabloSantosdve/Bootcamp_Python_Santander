# Dicionário de contatos com e-mails como chaves e outro dicionário como valor (nome e telefone)
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Método .clear() limpa o dicionário inteiro — apaga geral!
# Quando usar: se você quer resetar o dicionário, tipo zerar uma agenda ou limpar os dados da sessão.
contatos.clear()

# Agora o dicionário tá vazio: {}
# Isso é útil, por exemplo, em situações onde os dados antigos não são mais necessários.
print(contatos)  # {}
# Saída esperada: {}
# O dicionário foi limpo, então não tem mais nada dentro dele.