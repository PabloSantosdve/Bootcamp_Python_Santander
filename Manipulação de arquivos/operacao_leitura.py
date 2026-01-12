# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

# Abre o arquivo em modo leitura ("r")
arquivo = open(
    r"C:\Users\user\Documents\GitHub\bootcamp\bootcamp_python_santander\Manipulação de arquivos\lorem.txt", "r"
)
# Lê todo o conteúdo do arquivo de uma vez
print(arquivo.read())
# Fecha o arquivo
arquivo.close()

# Abre o arquivo novamente em modo leitura
arquivo = open(
    r"C:\Users\user\Documents\GitHub\bootcamp\bootcamp_python_santander\Manipulação de arquivos\lorem.txt", "r"

)
# Lê apenas a primeira linha do arquivo
print(arquivo.readline())
# Fecha o arquivo
arquivo.close()

# Abre o arquivo novamente
arquivo = open(
    r"C:\Users\user\Documents\GitHub\bootcamp\bootcamp_python_santander\Manipulação de arquivos\lorem.txt", "r"
)
# Lê todas as linhas do arquivo e retorna uma lista
print(arquivo.readlines())
# Fecha o arquivo
arquivo.close()

# Abre o arquivo novamente
arquivo = open(
    r"C:\Users\user\Documents\GitHub\bootcamp\bootcamp_python_santander\Manipulação de arquivos\lorem.txt", "r"
)
# Loop que lê linha por linha até acabar (usando operador walrus := do Python 3.8+)
while len(linha := arquivo.readline()):
    print(linha)
# Fecha o arquivo
arquivo.close()

"""
read()
Esse método lê todo o conteúdo do arquivo de uma vez só. Ele devolve tudo como uma única string.
É útil quando o arquivo é pequeno e você quer ver tudo junto.
Exemplo de uso: ler um texto completo de um arquivo .txt.

readline()
Lê uma linha por vez. Cada vez que você chama, ele pega a próxima linha.
É bom quando você quer processar o arquivo linha por linha, sem carregar tudo na memória.
Exemplo de uso: ler logs, onde você trata linha por linha.

readlines()
Lê todas as linhas de uma vez e guarda cada uma como um item de uma lista.
É útil se você quer trabalhar com todas as linhas, mas ainda quer elas separadas.
Exemplo de uso: contar linhas, filtrar conteúdo, etc.

for linha in arquivo
Esse é o jeito mais eficiente de ler linha por linha.
O Python já sabe que o arquivo é um iterador de linhas, então ele cuida de tudo por baixo dos panos.
Exemplo de uso: percorrer um arquivo grande sem travar seu programa.
"""
