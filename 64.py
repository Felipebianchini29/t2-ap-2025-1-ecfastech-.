def exercicio_64():
    mensagem = input("Digite a string original: ")
    caractere_antigo = input("Digite o caractere a ser substituído: ")
    caractere_novo = input("Digite o novo caractere: ")

    if len(caractere_antigo) != 1 or len(caractere_novo) != 1:
        print("Por favor, digite apenas um caractere para ambos o caractere antigo e o novo.")
        return
    
    nova_mensagem_lista = []
    for char in mensagem:
        if char == caractere_antigo:
            nova_mensagem_lista.append(caractere_novo)
        else:
            nova_mensagem_lista.append(char)
    nova_mensagem = "".join(nova_mensagem_lista)
    
    print(f"Mensagem original: \"{mensagem}\"")
    print(f"Nova mensagem: \"{nova_mensagem}\"")

