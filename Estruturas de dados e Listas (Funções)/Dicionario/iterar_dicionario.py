# Dicionário de contatos. A chave é o e-mail da pessoa,
# e o valor é outro dicionário com nome e telefone.
# Isso é útil quando você quer guardar informações organizadas por algum identificador único (nesse caso, o e-mail).
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Primeira forma de percorrer o dicionário: só com as chaves
# Aqui, você tá pegando cada chave (email) do dicionário e usando ela pra acessar o valor correspondente.
# Bom pra quando você só precisa da chave, ou quer fazer algo com base nela.
for chave in contatos:
    print(chave, contatos[chave])

# Separador visual, só pra deixar o print organizado no terminal
print("=" * 100)

# Segunda forma (mais chique): usando .items() pra pegar chave e valor ao mesmo tempo
# Isso retorna uma tupla (chave, valor) pra cada item do dicionário.
# Muito usado quando você quer trabalhar com ambos, tipo montar uma mensagem ou formatar os dados.
for chave, valor in contatos.items():
    print(chave, valor)
# Separador visual, só pra deixar o print organizado no terminal
print("=" * 100)
# Terceira forma: usando .keys() e .values()
# .keys() te dá só as chaves, e .values() só os valores.
for chave in contatos.keys():
    print(chave)
for valor in contatos.values():
    print(valor)
# Separador visual, só pra deixar o print organizado no terminal