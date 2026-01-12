# Interpolação de variáveis em Python
# -----------------------------------
# Interpolação é o processo de inserir valores de variáveis dentro de strings.
# Isso é útil quando queremos construir mensagens dinâmicas ou formatar dados de forma legível.
# Em Python, existem várias formas de fazer interpolação de strings:
# 1. Usando o operador % (estilo antigo)
# 2. Usando o método .format()
# 3. Usando f-strings (a forma mais moderna e recomendada desde o Python 3.6)

# Exemplo 1: Usando o operador %
nome = "Ana"
idade = 25
profissao = "Programador"
linguagem = "JAVA"

print("Meu nome é %s e eu tenho %d anos, minha profissão é %s e trabalho com linguagem %s." % (nome, idade, profissao, linguagem))

# Exemplo 2: Usando o método .format()
print("Meu nome é {} e eu tenho {} anos, minha profissão é {} e trabalho com linguagem {} .".format(nome, idade, profissao, linguagem))

# Usando índices numéricos para mudar a ordem das variáveis na string
print("Trabalho com {3}, sou {2}, me chamo {0} e tenho {1} anos.".format(nome, idade, profissao, linguagem))

#Usando o modo format com dicionario 
# Criando um dicionário com as informações
dados = {
    "nome": "Mariana",
    "idade": 28,
    "profissao": "designer",
    "linguagem": "JavaScript"
}

# Usando chaves nomeadas com .format(**dicionario)
print("Olá, meu nome é {nome}, tenho {idade} anos, sou {profissao} e trabalho com {linguagem}.".format(**dados))

# Definindo as variáveis
nome = "Fernanda"
idade = 27
profissao = "arquiteta"
cidade = "Curitiba"

# Usando .format() com nomes de variáveis
print("Olá, meu nome é {nome}, tenho {idade} anos, sou {profissao} e moro em {cidade}.".format(
    nome=nome,
    idade=idade,
    profissao=profissao,
    cidade=cidade
))


#----------------------------------
# Exemplo 3: Usando f-strings (forma moderna e mais legível)
print(f"Meu nome é {nome} e eu tenho {idade} anos, minha profissão é {profissao} e trabalho com linguagem {linguagem}.")

# Também é possível fazer expressões dentro de f-strings
print(f"Daqui a 5 anos, {nome} terá {idade + 5} anos, , minha profissão é {profissao} e trabalho com linguagem {linguagem}.")

# Cálculo direto dentro da f-string
print(f"Se eu receber um aumento de 10%, meu novo salário será R${salario * 1.10:.2f}.")





