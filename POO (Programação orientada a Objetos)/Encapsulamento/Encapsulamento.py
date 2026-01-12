# Classe Conta representa uma conta bancária simples
class Conta:

    # Método construtor (__init__) – chamado ao criar a conta
    # Conceito: INICIALIZAÇÃO DE OBJETOS + ENCAPSULAMENTO
    # O atributo _saldo é "protegido" (por convenção, com underline) — não deve ser acessado diretamente fora da classe
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo                # Atributo protegido (por convenção) — encapsulamento
        self.nro_agencia = nro_agencia     # Número da agência (público) 

    # Método público depositar
    # Conceito: INTERFACE PÚBLICA (método que altera um atributo interno)
    def depositar(self, valor):
        # Soma o valor ao saldo atual
        self._saldo += valor  # underline avisa: não mexe nisso de fora na malandragem 

    # Método público sacar
    # Conceito: INTERFACE PÚBLICA + ENCAPSULAMENTO
    def sacar(self, valor):
        # Subtrai o valor do saldo (sem validação aqui, só pra exemplo)
        self._saldo -= valor 

    # Método público para mostrar o saldo
    # Conceito: ENCAPSULAMENTO (acesso controlado a atributos internos)
    def mostrar_saldo(self):
        # Retorna o saldo atual de forma segura, sem expor diretamente o atributo
        return self._saldo


# Criando uma instância da classe Conta
# Conceito: INSTANCIAÇÃO DE OBJETO
conta = Conta("0001", 100)  # Agência 0001, saldo inicial 100

# Chamando o método depositar (adiciona 100 ao saldo)
conta.depositar(100)

# Imprimindo o número da agência — atributo público, acesso direto
print(conta.nro_agencia)

# Imprimindo o saldo — usando método para respeitar o encapsulamento
print(conta.mostrar_saldo())  # Esperado: 200
 
# Chamando o método sacar (subtrai 50 do saldo)
conta.sacar(50)
# Imprimindo o saldo novamente
print(conta.mostrar_saldo())  # Esperado: 150  