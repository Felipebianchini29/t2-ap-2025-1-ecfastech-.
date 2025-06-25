def exercicio_66():
    lista_palavras = []
    print("Digite as palavras uma por uma. Digite 'fim' para terminar a lista.")
    while True:
        palavra = input("Digite uma palavra (ou 'fim' para terminar): ").strip()
        if palavra.lower() == 'fim':
            break
        if len(palavra) > 0:
            lista_palavras.append(palavra)

    if not lista_palavras:
        print("Nenhuma palavra foi inserida.")
        return

    separador = input("Digite o caractere separador (ex: '-', ' ', '_'): ")
    
    string_unida = ""
    if len(lista_palavras) > 0:
        string_unida = lista_palavras[0]
        i = 1
        while i < len(lista_palavras):
            string_unida += separador + lista_palavras[i]
            i += 1
    
    print(f"Lista original de palavras: {lista_palavras}")
    print(f"Separador: '{separador}'")
    print(f"String unida: \"{string_unida}\"")

