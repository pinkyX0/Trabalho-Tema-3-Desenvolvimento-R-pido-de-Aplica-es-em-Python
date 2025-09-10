import math

def calcular_fatoriais(lista):
    for elemento in lista:
        try:
            # Verifica se é um número inteiro
            if not isinstance(elemento, int):
                raise TypeError(f"O elemento '{elemento}' não é um número inteiro.")

            # Verifica se é número negativo
            if elemento < 0:
                raise ValueError(f"O número {elemento} é negativo e não possui fatorial.")

            # Calcula o fatorial
            resultado = math.factorial(elemento)
            print(f"Fatorial de {elemento} = {resultado}")

        except TypeError as e:
            print(f"Erro: {e}")
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            # Tratamento de erro genérico
            print(f"Erro inesperado com o elemento {elemento}: {e}")


# Exemplo de uso
numeros = [5, 3, -2, "abc", 7]
calcular_fatoriais(numeros)
