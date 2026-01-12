from pathlib import Path

# Define o caminho raiz como o diretório onde o script está localizado
ROOT_PATH = Path(__file__).parent

# Tenta abrir o arquivo "1lorem.txt" para leitura
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        # Lê e imprime todo o conteúdo do arquivo
        print(arquivo.read())
# Captura qualquer erro de entrada/saída, como arquivo inexistente ou problema de permissão
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

# Bloco comentado — se ativado, criaria um arquivo com codificação UTF-8 e escreveria uma string nele
try:
     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
except IOError as exc:
     print(f"Erro ao abrir o arquivo {exc}")

# Tenta abrir o arquivo criado acima para leitura com codificação UTF-8
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
# Captura erros de leitura ou acesso
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
# Captura erro de decodificação de caracteres caso o conteúdo não esteja em UTF-8
except UnicodeDecodeError as exc:
    print(exc)
