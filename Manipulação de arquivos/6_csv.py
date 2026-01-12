import csv  # Módulo que facilita leitura e escrita de arquivos CSV
from pathlib import Path  # Biblioteca moderna para manipulação de caminhos de arquivos

# Define o caminho base do script atual
ROOT_PATH = Path(__file__).parent

# Constantes para acessar colunas específicas de forma mais legível
COLUNA_ID = 0
COLUNA_NOME = 1

# --- Escrita de arquivo CSV ---
try:
    # Abre (ou cria) o arquivo "usuarios.csv" para escrita ('w') com codificação UTF-8
    # newline="" evita problemas de quebra de linha no Windows
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)  # Cria um "escritor" de CSV, que escreve em formato de lista
        escritor.writerow(["id", "nome"])  # Cabeçalho do CSV
        escritor.writerow(["1", "Maria"])  # Primeira linha de dados
        escritor.writerow(["2", "João"])   # Segunda linha de dados
except IOError as exc:
    # Captura problemas ao tentar criar ou escrever no arquivo
    print(f"Erro ao criar o arquivo. {exc}")

# --- Leitura com csv.reader (retorna listas) ---
try:
    # Abre o mesmo arquivo CSV para leitura
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)  # Cria um "leitor" de CSV, que lê linhas como listas
        for idx, row in enumerate(leitor):  # Percorre cada linha com índice
            if idx == 0:
                continue  # Pula o cabeçalho
            print(f"ID: {row[COLUNA_ID]}")    # Acessa pelo índice a coluna ID
            print(f"Nome: {row[COLUNA_NOME]}")  # Acessa pelo índice a coluna nome
except IOError as exc:
    print(f"Erro ao ler o arquivo. {exc}")

# --- Leitura com csv.DictReader (retorna dicionários) ---
try:
    # Abre o mesmo arquivo para leitura, dessa vez usando DictReader
    # O DictReader usa automaticamente a primeira linha como chave (header)
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)  # Cada linha agora é um dicionário com chaves "id" e "nome"
        for row in reader:
            print(f"ID: {row['id']}")      # Acesso mais legível via chave
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao ler o arquivo. {exc}")
