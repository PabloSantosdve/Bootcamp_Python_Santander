contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# .pop(chave) remove a chave do dicionário e retorna o valor dela
# Se a chave existir → ela é removida e o valor é retornado
# É tipo um "pega e deleta"
resultado = contatos.pop("guilherme@gmail.com")  
print(resultado)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# Agora a chave já foi removida do dicionário, então ela não existe mais

# Se você tentar usar .pop() de novo com essa chave, sem passar valor padrão → vai dar KeyError
# MAS aqui passamos um valor padrão: {}
# Então, como a chave não existe, ele retorna esse valor padrão em vez de dar erro
resultado = contatos.pop("guilherme@gmail.com", {})  
print(resultado)  # {}
