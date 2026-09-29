def contar_palavras(texto):
    palavras = texto.strip().split()
    print(f"Total de palavras: {len(palavras)}")
    print(f"Total de caracteres: {len(texto)}")

# Exemplo rápido:
contar_palavras("E aí, beleza? Testando o contador de palavras.")
