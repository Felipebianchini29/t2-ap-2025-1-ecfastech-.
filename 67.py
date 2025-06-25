def exercicio_67():
    texto = input("Digite o texto principal: ")
    padrao = input("Digite a string padrão: ")
    
    # Verifica se o padrão é um prefixo
    e_prefixo = False
    if len(padrao) <= len(texto):
        todos_iguais = True
        i = 0
        while i < len(padrao):
            if texto[i] != padrao[i]:
                todos_iguais = False
                break
            i += 1
        if todos_iguais:
            e_prefixo = True
    
    # Verifica se o padrão é um sufixo
    e_sufixo = False
    if len(padrao) <= len(texto):
        todos_iguais = True
        i = 0
        while i < len(padrao):
            if texto[len(texto) - len(padrao) + i] != padrao[i]:
                todos_iguais = False
                break
            i += 1
        if todos_iguais:
            e_sufixo = True
    
    print(f"Texto: \"{texto}\"")
    print(f"Padrão: \"{padrao}\"")
    print(f"É '{padrao}' um prefixo de '{texto}'?: {e_prefixo}")
    print(f"É '{padrao}' um sufixo de '{texto}'?: {e_sufixo}")
