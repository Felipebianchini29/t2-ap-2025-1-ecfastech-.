def exercicio_63():
    string_entrada = input("Digite uma string com palavras separadas por espaços: ")
    
    contagem_palavras = 0
    no_palavra = False
    for char in string_entrada:
        if char != ' ':
            if not no_palavra:
                contagem_palavras += 1
                no_palavra = True
        else:
            no_palavra = False
    
    print(f"O número de palavras na string é: {contagem_palavras}.")