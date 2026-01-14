contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# Se você tentar acessar uma chave que não existe assim:
# contatos["chave"]  → vai dar erro (KeyError), porque a chave não tá no dicionário
# É o famoso: "mano, essa chave nem existe!"
# contatos["chave"]  # KeyError

# Usando .get(), o Python NÃO dá erro se a chave não existir
# Em vez disso, ele retorna None (ou o valor padrão que você quiser)
resultado = contatos.get("chave")  # chave não existe → retorna None
print(resultado)  # Saída: None

# Aqui passamos um valor padrão: {}
# Ou seja, se a chave não existir, ele retorna esse dicionário vazio
resultado = contatos.get("chave", {})  # chave não existe → retorna {}
print(resultado)  # Saída: {}

# Agora buscamos uma chave que EXISTE: "guilherme@gmail.com"
# Como ela tá no dicionário, .get() retorna o valor correspondente normalmente
resultado = contatos.get("guilherme@gmail.com", {})  
print(resultado)  # Saída: {'nome': 'Guilherme', 'telefone': '3333-2221'}
