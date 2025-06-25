def exercicio_32():
    while True:
        try:
            num = int(input("Fatorial de: "))
            if num >= 0:
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if num == 0:
        fatorial = 1
        expressao = "1"
    else:
        fatorial = 1
        lista_expressao = []
        for i in range(num, 0, -1):
            fatorial *= i
            lista_expressao.append(str(i))
        expressao = ".".join(lista_expressao)

    print(f"{num}! = {expressao} = {fatorial}")