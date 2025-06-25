def exercicio_33():
    temperaturas = []
    print("Digite as temperaturas. Digite 'fim' para finalizar.")
    while True:
        entrada_usuario = input("Digite a temperatura: ")
        if entrada_usuario.lower() == 'fim':
            break
        try:
            temp = float(entrada_usuario)
            temperaturas.append(temp)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if temperaturas:
        menor_temp = temperaturas[0]
        maior_temp = temperaturas[0]
        soma_temp = 0
        for temp in temperaturas:
            if temp < menor_temp:
                menor_temp = temp
            if temp > maior_temp:
                maior_temp = temp
            soma_temp += temp
        
        media_temp = soma_temp / len(temperaturas)
        print(f"\nMenor temperatura informada: {menor_temp:.2f}°C.")
        print(f"Maior temperatura informada: {maior_temp:.2f}°C.")
        print(f"Média das temperaturas: {media_temp:.2f}°C.")
    else:
        print("Nenhuma temperatura foi inserida.")

