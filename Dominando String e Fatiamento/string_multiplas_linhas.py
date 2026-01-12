# STRINGS DE MÚLTIPLAS LINHAS EM PYTHON
# -------------------------------------
# Em Python, strings de múltiplas linhas são úteis quando queremos armazenar ou exibir textos
# longos que ocupam mais de uma linha, como parágrafos, mensagens formatadas, ou até mesmo
# blocos de código. 
#
# Existem duas formas principais de criar strings com múltiplas linhas:
#
# 1. Usando aspas triplas (''' ou """):
#    - Permite escrever o texto exatamente como ele será exibido, com quebras de linha incluídas.
#    - Muito útil para docstrings, mensagens longas, ou quando queremos preservar a formatação.
#
# 2. Usando caracteres de escape (\n):
#    - Permite inserir quebras de linha dentro de uma string de linha única.
#    - Útil quando queremos controlar a formatação de forma mais programática.
#
# Strings de múltiplas linhas são especialmente úteis para mensagens de erro, textos explicativos,
# ou qualquer conteúdo que precise ser exibido de forma legível e estruturada.

# EXEMPLO 1: Usando aspas triplas
mensagem = """Olá, usuário!
Este é um exemplo de string
que ocupa várias linhas.
Muito útil para mensagens longas."""
print(mensagem)

# EXEMPLO 2: Usando \n para quebras de linha
mensagem2 = "Olá, usuário!\nEste é um exemplo de string\ncom quebras de linha usando \\n."
print(mensagem2)

# EXEMPLO 3: String de múltiplas linhas com interpolação (f-string)
nome = "Marcos"
aviso = f"""
Olá, {nome}!

Este é um aviso importante:
- Sua conta será atualizada em breve.
- Verifique seu e-mail para mais informações.

Atenciosamente,
Equipe de Suporte
"""
print(aviso)

nome = "Pablo"

mensagem3 = f"""Olá meu nome é {nome}
estou aprendendo Python.
Essa mensagem tem diferentes recuos"""

print(mensagem3)


"""
MENU DE CAIXA ELETRÔNICO
------------------------
Este é um exemplo simples de como exibir um menu de opções
em um caixa eletrônico usando Python. O usuário poderá escolher
uma das opções disponíveis para simular uma operação bancária.
"""

# Exibindo o menu
menu = """
===============================
     CAIXA ELETRÔNICO PYBANK
===============================
1 - Ver saldo
2 - Sacar dinheiro
3 - Depositar dinheiro
4 - Transferir
5 - Sair
===============================
"""

print(menu)

# Simulando a escolha do usuário
opcao = input("Escolha uma opção (1-5): ")

if opcao == "1":
    print("Seu saldo atual é R$ 1.250,00")
elif opcao == "2":
    print("Você escolheu sacar dinheiro.")
elif opcao == "3":
    print("Você escolheu depositar dinheiro.")
elif opcao == "4":
    print("Você escolheu transferir dinheiro.")
elif opcao == "5":
    print("Obrigado por usar o PyBank. Até logo!")
else:
    print("Opção inválida. Tente novamente.")
