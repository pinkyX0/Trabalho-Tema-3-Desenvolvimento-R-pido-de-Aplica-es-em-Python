def ler_nome():
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o que foi digitado realmente é uma string não vazia
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome inválido: não pode ser vazio.")

        print(f"Nome válido: {nome}")

    except ValueError as e:
        print(f"Erro: {e}")

# Executa a função
ler_nome()
