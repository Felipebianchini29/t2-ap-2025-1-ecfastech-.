def exercicio_71():
    def validar_email(email):
        contagem_arroba = 0
        for char in email:
            if char == '@':
                contagem_arroba += 1
        
        if contagem_arroba != 1:
            return False
        
        partes = []
        parte_atual = []
        for char in email:
            if char == '@':
                partes.append("".join(parte_atual))
                parte_atual = []
            else:
                parte_atual.append(char)
        partes.append("".join(parte_atual)) # Adiciona a parte do domínio

        parte_local = partes[0]
        parte_dominio = partes[1]

        if len(parte_local) == 0:
            return False
        
        if '.' not in parte_dominio:
            return False
        
        subpartes_dominio = []
        subparte_atual = []
        for char in parte_dominio:
            if char == '.':
                subpartes_dominio.append("".join(subparte_atual))
                subparte_atual = []
            else:
                subparte_atual.append(char)
        subpartes_dominio.append("".join(subparte_atual))

        if len(subpartes_dominio) == 0 or len(subpartes_dominio[0]) == 0:
            return False

        if len(subpartes_dominio[len(subpartes_dominio) - 1]) < 2:
            return False
        
        tem_ponto_duplo = False
        i = 0
        while i < len(parte_dominio) - 1:
            if parte_dominio[i] == '.' and parte_dominio[i+1] == '.':
                tem_ponto_duplo = True
                break
            i += 1
        if tem_ponto_duplo or parte_dominio[0] == '.' or parte_dominio[len(parte_dominio) - 1] == '.':
            return False

        return True

    while True:
        email_para_validar = input("Digite um endereço de e-mail para validar (ou 'fim' para finalizar): ")
        if email_para_validar.lower() == 'fim':
            break
        
        e_valido = validar_email(email_para_validar)
        print(f"E-mail '{email_para_validar}' é válido: {e_valido}.")

