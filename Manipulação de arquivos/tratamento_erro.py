from pathlib import Path  # Biblioteca moderna para trabalhar com caminhos de forma mais segura e orientada a objetos

# Define o caminho base como o diretório onde o script está salvo
# Isso garante que o código funcione corretamente em qualquer máquina, sem precisar de caminhos absolutos
ROOT_PATH = Path(__file__).parent

try:
    # Tenta abrir o arquivo "novo.txt" que está dentro do diretório "novo-diretorio", em modo de leitura ("r")
    # Se o arquivo existir e for acessível, ele será aberto com sucesso
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")

# Se o arquivo não for encontrado no caminho indicado, cai nesse bloco
# FileNotFoundError é uma exceção específica para arquivos ausentes
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")   # Mensagem clara para o usuário
    print(exc)  # Mostra a descrição técnica do erro (opcional, útil pra debugging)

# Se o caminho apontar para uma pasta (diretório) e não para um arquivo, esse erro é lançado
# Por exemplo: tentar abrir um diretório como se fosse um arquivo
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")

# Captura problemas de entrada/saída em geral, como falha de permissão, arquivo bloqueado, etc.
# IOError cobre erros que não são necessariamente "o arquivo não existe", mas relacionados ao acesso ao disco
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

# Captura qualquer outro erro que não foi tratado especificamente acima
# Isso garante que o programa não quebre inesperadamente
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

# --- Exemplo extra de uso do IsADirectoryError ---
# Esse trecho comentado mostra um caso prático de erro:
# Aqui o código tenta abrir um diretório como se fosse um arquivo, o que causa um IsADirectoryError

# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")