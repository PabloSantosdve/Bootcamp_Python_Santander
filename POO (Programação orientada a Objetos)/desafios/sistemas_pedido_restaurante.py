# ------------------------------------------------------------
# 💡 DESAFIO:
# Criar uma classe chamada Pedido que represente um pedido em um restaurante.
# Essa classe deve armazenar os itens pedidos (apenas os preços) e permitir calcular o total da conta.
#
# 🚀 Requisitos:
# - A classe deve ter um atributo para guardar os preços dos itens.
# - Deve possuir um método que calcula e retorna a soma dos preços.
#
# 🧾 Entrada:
# - Primeiro, o número de itens que serão pedidos (inteiro).
# - Depois, para cada item, uma linha contendo o nome do item e seu preço separado por espaço.
#
# 📤 Saída:
# - Um único valor, que é o total da conta, formatado com duas casas decimais.
#
# 🧪 Exemplos:
# Entrada:
# 2
# Pizza 40.00
# Suco 7.50
# Saída:
# 47.50
#
# Entrada:
# 3
# Hamburguer 15.50
# Refrigerante 5.00
# Batata 8.00
# Saída:
# 28.50
#
# Entrada:
# 4
# Café 4.50
# Pão de queijo 6.00
# Bolo 10.25
# Chá 3.75
# Saída:
# 24.50
#
# ------------------------------------------------------------

class Pedido:
    def __init__(self):
        # Lista para armazenar os preços dos itens do pedido
        self.itens = []  
    
    def adicionar_item(self, preco):
        # Adiciona o preço recebido na lista de itens
        self.itens.append(preco)

    def calcular_total(self):
        # Retorna a soma de todos os preços armazenados na lista
        return sum(self.itens)

# Lê a quantidade de pedidos que o usuário vai inserir
quantidade_pedidos = int(input().strip())

# Cria um objeto Pedido para armazenar os itens
pedido = Pedido()

# Loop para ler cada pedido
for _ in range(quantidade_pedidos):
    entrada = input().strip()  # Lê a linha do pedido (ex: "Pizza 40.00")
    nome, preco = entrada.rsplit(" ", 1)  # Separa o nome e o preço (rsplit do último espaço)
    preco_convertido = float(preco)  # Converte o preço pra float (número decimal)
    pedido.adicionar_item(preco_convertido)  # Adiciona o preço no pedido

# Calcula o total da conta somando os preços dos itens
total = pedido.calcular_total()

# Imprime o total formatado com duas casas decimais
print(f"{total:.2f}")
