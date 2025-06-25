def exercicio_69():
    def contar_palavras(lista_de_frases):
        contagem_palavras_dict = {}
        for frase in lista_de_frases:
            frase_limpa_caracteres = []
            for char in frase:
                if ('a' <= char.lower() <= 'z') or ('0' <= char <= '9'):
                    frase_limpa_caracteres.append(char.lower())
                else:
                    frase_limpa_caracteres.append(' ')
            frase_limpa = "".join(frase_limpa_caracteres)

            palavra_atual_list = []
            para_adicionar_palavra = False
            for char_limpo in frase_limpa:
                if char_limpo != ' ':
                    palavra_atual_list.append(char_limpo)
                    para_adicionar_palavra = True
                else:
                    if para_adicionar_palavra:
                        palavra = "".join(palavra_atual_list)
                        if palavra in contagem_palavras_dict:
                            contagem_palavras_dict[palavra] += 1
                        else:
                            contagem_palavras_dict[palavra] = 1
                        palavra_atual_list = []
                        para_adicionar_palavra = False
            
            if para_adicionar_palavra:
                palavra = "".join(palavra_atual_list)
                if palavra in contagem_palavras_dict:
                    contagem_palavras_dict[palavra] += 1
                else:
                    contagem_palavras_dict[palavra] = 1
        return contagem_palavras_dict

    frases_entrada = []
    print("Digite as frases uma por uma. Digite 'fim' em uma linha vazia para finalizar.")
    while True:
        linha = input("Digite a frase: ")
        if linha.lower() == 'fim' and not linha.strip():
            break
        if len(linha.strip()) > 0:
            frases_entrada.append(linha)

    if frases_entrada:
        contagens = contar_palavras(frases_entrada)
        print("\nContagem de palavras em todas as frases:")
        for palavra, contagem in contagens.items():
            print(f"'{palavra}': {contagem}")
    else:
        print("Nenhuma frase foi inserida.")


