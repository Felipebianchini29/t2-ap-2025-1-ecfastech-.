def exercicio_61():
    texto_com_espacos = input("Digite uma string com possivelmente espaços extras: ")
    
    palavras = []
    palavra_atual = []
    for char in texto_com_espacos:
        if char == ' ':
            if len(palavra_atual) > 0:
                palavras.append("".join(palavra_atual))
                palavra_atual = []
        else:
            palavra_atual.append(char)
    
    if len(palavra_atual) > 0:
        palavras.append("".join(palavra_atual))

    texto_limpo = ""
    if len(palavras) > 0:
        texto_limpo = palavras[0]
        for i in range(1, len(palavras)):
            texto_limpo += " " + palavras[i]
    
    print(f"Texto original: \"{texto_com_espacos}\"")
    print(f"Texto limpo: \"{texto_limpo}\"")