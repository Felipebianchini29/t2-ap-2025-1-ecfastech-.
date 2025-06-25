def exercicio_27():
    while True:
        try:
            quantidade_turmas = int(input("Digite a quantidade de turmas: "))
            if quantidade_turmas > 0:
                break
            else:
                print("A quantidade de turmas deve ser positiva.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    total_alunos = 0
    turmas_validas = 0

    for i in range(quantidade_turmas):
        while True:
            try:
                alunos_na_turma = int(input(f"Digite a quantidade de alunos para a turma {i+1} (máx 40): "))
                if 0 <= alunos_na_turma <= 40:
                    total_alunos += alunos_na_turma
                    turmas_validas += 1
                    break
                else:
                    print("A quantidade de alunos por turma não pode exceder 40.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    if turmas_validas > 0:
        media_alunos = total_alunos / turmas_validas
        print(f"O número médio de alunos por turma é: {media_alunos:.2f}.")
    else:
        print("Nenhuma turma válida foi inserida.")
