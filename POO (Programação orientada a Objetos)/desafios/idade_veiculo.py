# ------------------------------------------------------------
# 💡 DESAFIO:
# Implementar uma classe chamada Veiculo que represente um carro.
# Essa classe deve conter os seguintes atributos:
# - marca (str)
# - modelo (str)
# - ano (int)
#
# Além disso, deve conter um método chamado verificar_antiguidade()
# que avalie se o carro é antigo (com base no ano atual).
#
# 🚗 Regras de negócio:
# - Um carro é considerado "antigo" se tiver mais de 20 anos.
# - Caso contrário, ele é considerado "novo".
#
# 🧾 Entrada:
# - Três valores fornecidos pelo usuário: marca, modelo e ano do veículo.
#
# 📤 Saída esperada:
# - A string "Veículo antigo" se o carro tiver mais de 20 anos.
# - A string "Veículo novo" caso contrário.
#
# 🧪 Exemplos:
# Entrada:
# Toyota
# Corolla
# 2000
# Saída:
# Veículo antigo
#
# Entrada:
# Honda
# Civic
# 2005
# Saída:
# Veículo novo
#
# Entrada:
# Ford
# Fiesta
# 1999
# Saída:
# Veículo antigo
#
# ------------------------------------------------------------


from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
  
    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
    
  def verificar_antiguidade(self):
    _ano_atual = datetime.now().year
      
    idade_veiculo = _ano_atual - self.ano
      
    if idade_veiculo > 20:
      return "Veículo antigo"
    else:
      return "Veículo novo"
      
# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())