# FUNÇÕES EM PYTHON

# Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica.
# Ela é usada para organizar o código, evitar repetições e facilitar a manutenção.
# Podemos definir uma função usando a palavra-chave 'def', seguida do nome da função e parênteses.
# Dentro dos parênteses, podemos definir parâmetros (valores que a função pode receber).
# O código dentro da função só é executado quando ela é chamada.

# Exemplo simples de função:
def saudacao():
    print("Olá! Seja bem-vindo(a).")

# Chamando a função:
saudacao()

# Exemplo com parâmetros:
def apresentar(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função com argumentos:
apresentar("Guilherme", 28)

# Também podemos fazer funções que retornam valores:
def somar(a, b):
    return a + b

# Armazenando o resultado da função em uma variável:
resultado = somar(5, 3)
print("Resultado da soma:", resultado)



# Função simples que não recebe nada e só imprime "Olá mundo!"
def exibir_mensagem():
    print("Olá mundo!")

# Função que recebe um parâmetro obrigatório 'nome'
# Imprime uma mensagem personalizada usando o nome passado
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# Função com parâmetro padrão
# Se 'nome' não for passado, usa "Anônimo" como padrão
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Chamadas das funções:
exibir_mensagem()                 # Imprime: Olá mundo!
exibir_mensagem_2(nome="Guilherme")  # Imprime: Seja bem vindo Guilherme!
exibir_mensagem_3()               # Sem argumento, usa padrão → Seja bem vindo Anônimo!
exibir_mensagem_3(nome="Chappie")    # Passa argumento → Seja bem vindo Chappie!
# Função com múltiplos parâmetros
def exibir_mensagem_4(nome, sobrenome):
    print(f"Seja bem vindo {nome} {sobrenome}!")    
# Chamada da função com múltiplos parâmetros
exibir_mensagem_4(nome="Guilherme", sobrenome="Silva")
# Função com múltiplos parâmetros e ordem diferente
def exibir_mensagem_5(sobrenome, nome):
    print(f"Seja bem vindo {nome} {sobrenome}!")
# Chamada da função com ordem diferente dos parâmetros
exibir_mensagem_5(nome="Guilherme", sobrenome="Silva") 


nome = input("Digite o seu nome: ")

def ola(nome):
    print(f"Ola, seja bem vindo {nome}")

ola(nome = nome)