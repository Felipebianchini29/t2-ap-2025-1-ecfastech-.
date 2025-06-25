def exercicio_22():
    while True:
        try:
            num = int(input("Digite um número inteiro para verificar se é primo: "))
            if num >= 0:
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if num <= 1:
        print(f"{num} não é um número primo.")
    else:
        e_primo = True
        divisores = []
        for i in range(2, num):
            if num % i == 0:
                e_primo = False
                divisores.append(i)
        if e_primo:
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")
            print(f"É divisível por: {divisores}.")
