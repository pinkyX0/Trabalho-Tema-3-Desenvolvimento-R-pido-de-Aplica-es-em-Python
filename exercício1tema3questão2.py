def dividir_numeros():
    try:
        # Leitura dos números
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        # Tentativa de divisão
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")

    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    except ValueError:
        print("Erro: Você deve digitar apenas números inteiros.")
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")


# Executa a função
dividir_numeros()
