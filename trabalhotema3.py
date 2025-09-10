def ler_nome():
    try:
        nome = input("Digite seu nome: ")

        # Se o nome estiver vazio ou só com espaços, dispara exceção
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")

        # Se tiver algum caractere que não seja letra ou espaço, dispara exceção
        if not all(c.isalpha() or c.isspace() for c in nome):
            raise ValueError("O nome deve conter apenas letras e espaços.")

        print(f"Nome válido: {nome}")

    except ValueError as erro:
        print(f"Erro: {erro}")

# Executa a função
ler_nome()

