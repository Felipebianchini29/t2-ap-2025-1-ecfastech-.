def exercicio_59():
    texto = input("Digite uma string: ")
    
    vogais = "aeiouAEIOU"
    contagem_vogais = 0
    contagem_consoantes = 0

    for char in texto:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            e_vogal = False
            for v in vogais:
                if char == v:
                    e_vogal = True
                    break
            if e_vogal:
                contagem_vogais += 1
            else:
                contagem_consoantes += 1
    
    print(f"Número de vogais: {contagem_vogais}.")
    print(f"Número de consoantes: {contagem_consoantes}.")
