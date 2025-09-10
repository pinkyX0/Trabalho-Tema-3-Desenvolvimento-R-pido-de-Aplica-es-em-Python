import os
import string

# 1) Ler ou criar arquivo
def exercicio1():
    nome_arquivo = "notas.txt"
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        print("Conteúdo de notas.txt:\n", conteudo)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Criando...")
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("Arquivo criado.")
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        print("Conteúdo após criação:\n", conteudo)


# 2) Contar linhas não vazias
def exercicio2():
    nome_arquivo = "frases.txt"
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
        qtd = sum(1 for linha in linhas if linha.strip())
        print(f"Linhas não vazias em '{nome_arquivo}': {qtd}")
    except PermissionError:
        print(f"Erro: sem permissão para abrir '{nome_arquivo}'.")


# 3) Normalizar espaços e pontos
def exercicio3():
    entrada = "comentarios.txt"
    saida = "comentarios_limpos.txt"
    conteudo = None

    try:
        with open(entrada, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except UnicodeDecodeError:
        try:
            with open(entrada, "r", encoding="latin-1") as f:
                conteudo = f.read()
        except Exception as e:
            print("Erro ao ler arquivo em latin-1:", e)

    if conteudo is not None:
        texto_limpo = conteudo.replace("  ", " ").replace("...", ".")
        with open(saida, "w", encoding="utf-8") as f:
            f.write(texto_limpo)
        print(f"Arquivo limpo salvo em '{saida}'.")


# 4) Nome e time separados por vírgula
def exercicio4():
    entrada = "jogadores_times.txt"
    log_invalido = "linhas_invalidas.log"
    jogadores = {}

    try:
        with open(entrada, "r", encoding="utf-8") as f:
            for linha in f:
                try:
                    if "," in linha:
                        nome, time = linha.strip().split(",", 1)
                        jogadores[nome.strip()] = time.strip()
                    else:
                        raise ValueError("Linha inválida (sem vírgula).")
                except Exception:
                    try:
                        with open(log_invalido, "a", encoding="utf-8") as log:
                            log.write(linha)
                    except Exception as e:
                        print("Erro ao registrar linha inválida:", e)
    except FileNotFoundError:
        print(f"Arquivo '{entrada}' não encontrado.")

    print("Dicionário de jogadores:", jogadores)


# 5) Dados ordenados
def exercicio5():
    arquivos = ["lista_a.txt", "lista_b.txt"]
    itens = set()

    for arq in arquivos:
        try:
            with open(arq, "r", encoding="utf-8") as f:
                itens.update(l.strip() for l in f if l.strip())
        except FileNotFoundError:
            print(f"Aviso: arquivo '{arq}' não encontrado.")

    itens_ordenados = sorted(itens)
    with open("lista_uniq.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(itens_ordenados))
    print("Arquivo 'lista_uniq.txt' gerado.")


# 6) Palavras únicas
def exercicio6():
    entrada = "texto.txt"
    try:
        with open(entrada, "r", encoding="utf-8") as f:
            texto = f.read().lower()
        # Remove pontuação simples
        for p in string.punctuation:
            texto = texto.replace(p, "")
        palavras = set(texto.split())
        print(f"Palavras únicas em '{entrada}': {len(palavras)}")
    except FileNotFoundError:
        print("Arquivo texto.txt não encontrado.")


# 7) Mesclar listas sem duplicatas
def exercicio7():
    arquivos = ["lista_a.txt", "lista_b.txt"]
    itens = set()

    for arq in arquivos:
        try:
            with open(arq, "r", encoding="utf-8") as f:
                itens.update(l.strip() for l in f if l.strip())
        except FileNotFoundError:
            print(f"Aviso: arquivo '{arq}' não encontrado.")

    itens_ordenados = sorted(itens)
    with open("lista_unica.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(itens_ordenados))
    print("Arquivo 'lista_unica.txt' gerado.")

