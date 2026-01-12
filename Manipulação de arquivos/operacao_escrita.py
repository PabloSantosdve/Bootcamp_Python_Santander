# Abre (ou cria) o arquivo em modo escrita ("w")
# Se o arquivo já existir, ele será sobrescrito
arquivo = open(
    r"C:\Users\user\Documents\GitHub\bootcamp\bootcamp_python_santander\Manipulação de arquivos\teste.txt", "w"
)

# Escreve uma única string no arquivo
arquivo.write("Escrevendo dados em um novo arquivo.")

# Escreve várias strings (como lista) no arquivo
# Cada item da lista é escrito na sequência
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

# Fecha o arquivo (sempre obrigatório para garantir que os dados sejam gravados corretamente)
arquivo.close()

"""
write()
O write() escreve texto direto no arquivo, como uma string só.
Você decide exatamente o que escrever, e se quiser pular linha, tem que colocar \n manualmente.

writelines()
O writelines() escreve várias linhas de uma vez, a partir de uma lista de strings.
Mas cuidado: ele não adiciona quebra de linha sozinho. As strings na lista já têm que ter \n no final.
"""