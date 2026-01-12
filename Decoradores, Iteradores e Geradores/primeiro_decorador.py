# Definindo o decorador na moralzinha
def meu_decorador(funcao):
    # Função interna que embrulha a original
    def envelope():
        print("faz algo antes de executar")  # Antes da função original
        funcao()  # Execução da função original
        print("faz algo depois de executar")  # Depois da função original

    return envelope  # Retorna o "pacote" decorado

# Função original, pura e simples
def ola_mundo():
    print("Olá mundo!")

# Aqui é onde o bicho pega: aplicando o decorador na mão
# A função ola_mundo é passada como argumento pro decorador
# E o resultado (a função envelope) substitui a original
ola_mundo = meu_decorador(ola_mundo)

# Agora quando tu chama ola_mundo(), tá chamando envelope()
ola_mundo()

def decorador(presente):
    def embrulho():
        print("Antes: coloca o laço no presente")
        presente()
        print("Depois: entrega com um sorriso")
    return embrulho

def dar_presente():
    print("Aqui está seu presente!")

# Embrulha o presente
dar_presente = decorador(dar_presente)

# Agora, quando você entrega o presente, tem todo o ritual
dar_presente()


def garcom(funcao_do_cozinheiro):
    def processo():
        print("Anota o pedido")
        funcao_do_cozinheiro()
        print("Entrega o prato com um 'bom apetite!'")
    return processo

def cozinheiro():
    print("Prato pronto!")

cozinheiro = garcom(cozinheiro)

cozinheiro()


def precisa_estar_logado(funcao):
    def wrapper():
        if not usuario_logado:
            print("Acesso negado: você precisa estar logado.")
            return
        funcao()
    return wrapper

# Simula se o usuário está logado ou não
usuario_logado = False

@precisa_estar_logado
def ver_dados_secretos():
    print("Aqui estão os dados secretos!")

ver_dados_secretos()  # Não vai deixar

# Agora o usuário se loga
usuario_logado = True

ver_dados_secretos()  # Agora deixa
"""
O que rolou aqui:
Tu manualmente decorou a função ola_mundo.
ola_mundo virou envelope na prática, mas o nome continuou o mesmo.
Esse é o mesmo efeito que usar @meu_decorador logo acima da definição.


Se quiser subir de nível depois, bora fazer:
Decorador com argumentos (@logar(tipo="INFO"))
Decorador que funciona com qualquer função (*args, **kwargs
"""