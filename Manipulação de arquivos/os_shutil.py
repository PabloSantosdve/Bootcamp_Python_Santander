import os
import shutil
from pathlib import Path  # Módulo moderno para trabalhar com caminhos de forma orientada a objetos

# Obtém o caminho da pasta onde o script está sendo executado
# Isso garante que os caminhos criados serão relativos ao local do arquivo .py
ROOT_PATH = Path(__file__).parent

# Define o caminho de um novo diretório chamado "novo-diretorio", que será criado dentro da pasta do script
novo_diretorio = ROOT_PATH / "novo-diretorio"

# Cria o diretório "novo-diretorio" se ele ainda não existir
# 'exist_ok=True' evita erro se o diretório já existir (boa prática ao criar pastas)
novo_diretorio.mkdir(exist_ok=True)

# Define o caminho completo do arquivo que será criado ("novo.txt") dentro do diretório raiz
arquivo_origem = ROOT_PATH / "novo.txt"

# Define o caminho para onde o arquivo será movido (dentro de "novo-diretorio")
arquivo_destino = novo_diretorio / "novo.txt"

# Abre (ou cria) o arquivo "novo.txt" em modo de escrita ("w") e escreve uma linha de texto
# Se o arquivo já existir, será sobrescrito
# Esse é um exemplo de manipulação de arquivos com escrita básica
with open(arquivo_origem, "w") as f:
    f.write("Conteúdo de teste\n")

# Verifica se o arquivo de origem realmente existe antes de tentar mover
# Isso evita erros em tempo de execução, como FileNotFoundError
if arquivo_origem.exists():
    # Move o arquivo de "arquivo_origem" para "arquivo_destino"
    # Aqui entra o uso do módulo 'shutil', útil para operações de alto nível com arquivos e diretórios
    shutil.move(arquivo_origem, arquivo_destino)
    print("Arquivo movido com sucesso.")
else:
    # Caso o arquivo não exista, exibe mensagem informando o problema
    # Boa prática para feedback ao usuário ou para debug
    print("Arquivo não encontrado.")
