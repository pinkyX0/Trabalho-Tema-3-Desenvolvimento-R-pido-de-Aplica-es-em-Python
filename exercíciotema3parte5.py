import os

def salvar_nome_em_arquivo(nome_arquivo):
    try:
        # Lê o nome completo
        nome = input("Digite seu nome completo: ")

        # Validação do nome
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        if not all(c.isalpha() or c.isspace() for c in nome):
            raise ValueError("O nome deve conter apenas letras e espaços.")

        # Converte para iniciais maiúsculas
        nome_formatado = nome.title()

        # Verifica se o arquivo está no diretório atual
        if not os.path.isdir(os.getcwd()):
            raise FileNotFoundError("Diretório inválido.")

        # Grava no arquivo
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(nome_formatado)

        print(f"Nome '{nome_formatado}' salvo em '{nome_arquivo}' com sucesso!")

    except ValueError as e:
        print(f"Erro de validação: {e}")
    except FileNotFoundError as e:
        print(f"Erro de diretório/arquivo: {e}")
    except PermissionError:
        print("Erro: Permissão negada para gravar no arquivo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Exemplo de uso
salvar_nome_em_arquivo("nome.txt")
