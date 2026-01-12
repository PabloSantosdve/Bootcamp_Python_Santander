"""
Operadores de Associação em Python

No universo da programação, é fundamental saber como verificar se um elemento está presente dentro de uma coleção, como uma lista, tupla ou até mesmo uma string. É aqui que entram os operadores de associação.

Os operadores de associação são 'in' e 'not in'. Eles são usados para testar a presença (ou ausência) de um valor dentro de uma sequência ou conjunto de elementos.

- O operador 'in' retorna True se o elemento procurado estiver contido na coleção.
- Já o operador 'not in' retorna True quando o elemento não está presente.

Por exemplo, imagine uma lista de frutas. Com o operador 'in', podemos verificar se uma fruta específica está nessa lista. Isso facilita a tomada de decisões em programas, tornando o código mais expressivo e fácil de entender.

Estes operadores são amplamente utilizados para validações, buscas e controle de fluxo, sendo ferramentas essenciais no arsenal de qualquer programador Python.
"""


# Exemplo de operador de associação 'in' e 'not in'

frutas = ["maçã", "banana", "laranja"]

# Verifica se 'banana' está na lista frutas
print("banana" in frutas)   # Vai imprimir: True

# Verifica se 'uva' está na lista frutas
print("uva" in frutas)      # Vai imprimir: False

# Verifica se 'uva' não está na lista frutas
print("uva" not in frutas)  # Vai imprimir: True

# Verifica se 'maçã' não está na lista frutas
print("maçã" not in frutas) # Vai imprimir: False


