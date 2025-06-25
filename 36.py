def exercicio_36():
    while True:
        try:
            numero = int(input("Montar a tabuada de: "))
            inicio = int(input("Começar por: "))
            fim = int(input("Terminar em: "))

            if inicio > fim:
                print("Erro: O valor final não pode ser menor que o inicial. Por favor, tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

    print(f"\nVou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{numero} X {i} = {numero * i}")