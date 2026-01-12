# Um dicionário em Python é uma estrutura de dados que armazena pares de chave-valor.
# Ele é muito útil quando queremos associar uma informação (valor) a uma identificação única (chave).
# Por exemplo, podemos usar um dicionário para representar uma pessoa, onde as chaves são os atributos
# como "nome", "idade" e "telefone", e os valores são os dados correspondentes.
# Dicionários são mutáveis, ou seja, podemos adicionar, remover ou modificar seus elementos após a criação.

# Criando um dicionário com os dados de uma pessoa
pessoa = {
    "nome": "Pablo",
    "idade": 22
}

# Substituindo o conteúdo do dicionário com novos dados
pessoa = dict(nome="Guilherme", idade=28)

# Adicionando uma nova chave "telefone" com seu respectivo valor
pessoa["telefone"] = "3333-1234"
