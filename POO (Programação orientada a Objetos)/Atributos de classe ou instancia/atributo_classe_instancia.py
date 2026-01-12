# Classe Estudante definida com um atributo de classe 'escola'
class Estudante:
    escola = "DIO"  # Atributo de classe, compartilhado por todos os objetos dessa classe

    def __init__(self, nome, matricula):
        self.nome = nome            # Atributo de instância: nome do estudante
        self.matricula = matricula  # Atributo de instância: número de matrícula

    def __str__(self) -> str:
        # Método que define como o objeto será representado como string (ex: no print)
        return f"{self.nome} - {self.matricula} - {self.escola}"


# Função que recebe vários objetos e imprime cada um
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)  # Aqui o método __str__ é chamado automaticamente


# Criando dois estudantes com a escola padrão ("DIO")
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

# Mostrando os valores dos dois primeiros estudantes
mostrar_valores(aluno_1, aluno_2)

# Alterando o valor do atributo de classe 'escola' para "Python"
Estudante.escola = "Python"

# Criando um novo estudante depois da alteração da escola
aluno_3 = Estudante("Chappie", 3)

# Mostrando todos os estudantes de novo (note que todos refletem a mudança da escola)
mostrar_valores(aluno_1, aluno_2, aluno_3)


"""
Ponto chave: Como escola é um atributo de classe, todos os objetos compartilham esse valor. Então quando a gente muda Estudante.escola, o valor é alterado pra todo mundo, mesmo pros objetos criados antes da mudança.

Se quiser fazer com que cada aluno tenha sua própria escola, aí tem que mover esse atributo pro __init__, tornando ele um atributo de instância (self.escola)
"""