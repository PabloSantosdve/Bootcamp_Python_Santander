# ARGUMENTOS NOMEADOS EM FUNÇÕES PYTHON

# Argumentos nomeados (ou argumentos com nome) são usados ao chamar uma função,
# especificando explicitamente o nome do parâmetro e o valor que queremos passar.
# Isso torna o código mais legível e evita erros com a ordem dos argumentos.

# Exemplo de função com três parâmetros:
def apresentar(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# Podemos chamar a função passando os argumentos na ordem correta:
apresentar("Maria", 30, "São Paulo")

# Ou podemos usar argumentos nomeados, o que permite mudar a ordem:
apresentar(nome="João", cidade="Rio de Janeiro", idade=25)

# Vantagens dos argumentos nomeados:
# - O código fica mais claro e fácil de entender
# - A ordem dos argumentos pode ser alterada
# - É útil quando a função tem muitos parâmetros

# Também é possível combinar argumentos posicionais e nomeados,
# mas os nomeados devem vir depois dos posicionais:
apresentar("Ana", idade=22, cidade="Curitiba")



# Função que recebe dados do carro e simula salvar no banco (só imprime mensagem)
def salvar_carro(marca, modelo, ano, placa):
    # Aqui normalmente rolaria código pra salvar no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Chamada 1: passando os argumentos na ordem tradicional, sem nomear
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Chamada 2: passando argumentos nomeados (keyword arguments)
# Dá pra passar em qualquer ordem quando usa nome
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# USANDO O OPERADOR ** PARA DESEMPACOTAR DICIONÁRIOS EM FUNÇÕES

# Suponha que temos uma função que recebe vários parâmetros:
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo: {marca} {modelo}, {ano}, placa {placa}")

# Temos também um dicionário com os dados de um carro:
dados = {
    "marca": "Fiat",
    "modelo": "Palio",
    "ano": 1999,
    "placa": "ABC-1234"
}

# Podemos passar esse dicionário para a função usando o operador **.
# Isso é chamado de "desempacotamento de dicionário".
# O Python irá transformar cada par chave-valor do dicionário em um argumento nomeado:
# Equivale a escrever: salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**dados)

# VANTAGENS:
# - Permite passar muitos argumentos de forma dinâmica e organizada
# - Muito útil quando os dados já estão em um dicionário (como em APIs, formulários, arquivos JSON etc.)
# - Deixa o código mais limpo, reutilizável e flexível

