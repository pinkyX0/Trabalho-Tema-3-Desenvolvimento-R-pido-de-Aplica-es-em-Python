import os

def contar_palavras_linhas(nome_arquivo):
    try:
        # Verifica se o arquivo existe no diretório atual
        if not os.path.isfile(nome_arquivo):
            raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")

        # Abre o arquivo em modo leitura
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        # Conta linhas
        qtd_linhas = len(linhas)

        # Conta palavras (separando por espaços em cada linha)
        qtd_palavras = sum(len(linha.split()) for linha in linhas)

        print(f"Total de linhas: {qtd_linhas}")
        print(f"Total de palavras: {qtd_palavras}")

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except PermissionError:
        print(f"Erro: Permissão negada para abrir o arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Exemplo de uso
arquivo = "meu_arquivo.txt"  # troque pelo nome do seu arquivo
contar_palavras_linhas(arquivo)
