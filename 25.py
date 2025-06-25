def exercicio_25():
    idades = []
    while True:
        try:
            n = int(input("Digite o número de pessoas: "))
            if n > 0:
                break
            else:
                print("O número de pessoas deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    for i in range(n):
        while True:
            try:
                idade = int(input(f"Digite a idade da pessoa {i+1}: "))
                if idade >= 0:
                    idades.append(idade)
                    break
                else:
                    print("A idade não pode ser negativa.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    if idades:
        soma_idades = 0
        for idade in idades:
            soma_idades += idade
        media_idade = soma_idades / len(idades)
        print(f"Idade média da turma: {media_idade:.2f}.")

        if 0 <= media_idade <= 25:
            print("A turma é jovem.")
        elif 26 <= media_idade <= 60:
            print("A turma é adulta.")
        else:
            print("A turma é idosa.")
    else:
        print("Nenhuma idade foi digitada.")