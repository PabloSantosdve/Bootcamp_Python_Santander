# Modo interativo do Python
# O modo interativo do Python permite que você execute comandos e veja os resultados imediatamente. 


# dir mostra os atributos e métodos disponíveis em um objeto
print(dir([]))  # Mostra métodos de uma lista
print(dir(str)) # Mostra métodos da classe string

# help exibe a documentação (docstring) de um objeto, função, módulo, etc
help(list.append)  # Mostra a documentação do método append da lista
help(str.upper)    # Mostra a documentação do método upper da string

# type retorna o tipo de um objeto
print(type([]))  # Mostra que é uma lista
print(type(str)) # Mostra que é uma classe string
# id retorna o identificador único de um objeto na memória
print(id([]))  # Mostra o identificador da lista
print(id(str)) # Mostra o identificador da classe string
# isinstance verifica se um objeto é uma instância de uma classe ou tipo específico
print(isinstance([], list))  # Verifica se é uma lista
print(isinstance(str, type)) # Verifica se é uma classe

# issubclass verifica se uma classe é uma subclasse de outra    
print(issubclass(list, object))  # Verifica se list é uma subclasse de object
print(issubclass(str, object))   # Verifica se str é uma subclasse de object

"""
 
 dir, help, type, id, isinstance e issubclass são funções built-in do Python, ou seja, já estão disponíveis por padrão e não precisam ser importadas de módulos externos.

 """


