contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# .popitem() remove e retorna o **último item** (chave e valor) do dicionário como uma tupla
# Se o dicionário tiver só um item, ele remove esse item e retorna ele
resultado = contatos.popitem()
print(resultado)  
# Saída: ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})

# Agora o dicionário está vazio

# Se você chamar .popitem() num dicionário vazio, dá KeyError (porque não tem nada pra remover)
# contatos.popitem()  # KeyError
