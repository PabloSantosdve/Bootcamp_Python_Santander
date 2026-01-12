# Importando ABC e abstractmethod para criar classes e métodos abstratos
from abc import ABC, abstractmethod

# Criando a classe base abstrata - o molde que obriga subclasses a implementarem certos métodos e propriedades
class ControleRemoto(ABC):  # Herda de ABC, o que torna essa classe abstrata

    @abstractmethod  # Método obrigatório para ligar o controle
    def ligar(self):
        # Aqui só tem o contrato, não tem implementação
        # Toda subclasse precisa implementar esse método com seu jeito
        pass

    @abstractmethod  # Método obrigatório para desligar o controle
    def desligar(self):
        # Também só o contrato, sem código aqui
        pass

    @property  # Define 'marca' como propriedade (acessada sem parênteses)
    @abstractmethod  # Torna obrigatório implementar essa propriedade nas subclasses
    def marca(self):
        # Esse é o contrato para a propriedade 'marca'
        # A subclasse precisa retornar o valor da marca aqui
        pass


# Classe concreta que herda de ControleRemoto e implementa tudo que é obrigatório
class ControleTV(ControleRemoto):

    def ligar(self):
        # Implementação concreta: o que acontece quando liga a TV
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        # Implementação concreta: o que acontece quando desliga a TV
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        # Implementa a propriedade obrigatória, retornando a marca da TV
        return "Philco"


# Outra classe concreta, agora para controle de Ar Condicionado
class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


# Aqui criamos uma instância de ControleTV
controle = ControleTV()

# Chamando métodos que a classe teve que implementar
controle.ligar()
controle.desligar()     

# Acessando a propriedade 'marca' da instância de ControleTV
print(controle.marca)  # Saída: Philco


# Criando uma instância de ControleArCondicionado
controle = ControleArCondicionado()

# Chamando os métodos dessa classe também
controle.ligar()
controle.desligar()

# Imprimindo a marca do ar condicionado
print(controle.marca)  # Saída: LG


# ---------------------------
# IMPORTANTE:
# 1. Você **não pode criar uma instância** de ControleRemoto diretamente,
#    porque é uma classe abstrata — ela tem métodos que são só contratos.
#
# 2. Se uma subclasse NÃO implementar todos os métodos e propriedades abstratas,
#    Python vai bloquear a criação da instância, gerando erro.
#
# 3. Esse mecanismo obriga a padronização — todo controle remoto tem que ter ligar,
#    desligar e marca, mas o jeito que faz isso pode mudar.
#
# 4. A propriedade abstrata com @property + @abstractmethod é o jeito moderno,
#    que substitui o antigo @abstractproperty que tá deprecated.
#
# 5. Assim, você consegue garantir que qualquer controle remoto (TV, ar,
#    videogame, etc) siga o mesmo “contrato” e tenha essas funcionalidades.


