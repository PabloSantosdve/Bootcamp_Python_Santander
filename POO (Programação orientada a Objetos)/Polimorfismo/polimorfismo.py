# Classe base Passaro com método voar
# Conceito: HERANÇA — outras classes vão herdar esse comportamento
class Passaro:
    def voar(self):
        print("Voando...")

# Classe Pardal herda de Passaro
# Conceito: SOBRESCRITA DE MÉTODO (polimorfismo)
# Pardal muda o comportamento do método voar para algo mais específico
class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

# Classe Avestruz herda de Passaro, mas avestruz não voa
# Aqui tem um problema no design: método voar existe, mas não faz sentido para avestruz
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# Exemplo ruim: Aviao herdando de Passaro só pra "ganhar" o método voar
# Conceito: HERANÇA FORÇADA (não é um pássaro, não devia herdar Passaro)
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

# Função que recebe qualquer objeto e chama o método voar
# Conceito: POLIMORFISMO — objetos diferentes respondem ao mesmo método de forma própria
def plano_voo(obj):
    obj.voar()

# Testando o polimorfismo — cada objeto voa do seu jeito
plano_voo(Pardal())    # Pardal pode voar
plano_voo(Avestruz())  # Avestruz não pode voar (mas tem método voar que não faz sentido aqui)
plano_voo(Aviao())     # Avião está decolando...



"""
Conceito: POLIMORFISMO
O polimorfismo permite que métodos com o mesmo nome tenham comportamentos diferentes dependendo do objeto que está usando.
Isso é útil quando várias classes diferentes precisam oferecer ações semelhantes, mas com implementações próprias.
Por exemplo, um método falar() pode existir tanto na classe Cachorro quanto na classe Gato, mas cada um "fala" de um jeito diferente ("Au au" vs "Miau").
Assim, você pode chamar o mesmo método em objetos diferentes sem se preocupar com o tipo, e cada um responde da sua maneira.
Isso simplifica o código e favorece a extensibilidade, já que novas classes podem ser adicionadas sem precisar reescrever lógica antiga.
É uma forma poderosa de aplicar o princípio da substituição de Liskov, mantendo o código mais genérico, flexível e fácil de manter.
"""