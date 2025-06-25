def exercicio_39():
    dados_alunos = []
    print("Digite os dados para 10 alunos (número do aluno, altura em centímetros).")

    for i in range(10):
        while True:
            try:
                numero_aluno = int(input(f"\nDigite o número do aluno {i+1}: "))
                altura_cm = float(input(f"Digite a altura do aluno {i+1} em cm: "))

                if numero_aluno <= 0 or altura_cm <= 0:
                    print("Número do aluno e altura devem ser positivos. Por favor, redigite para este aluno.")
                    continue
                
                dados_alunos.append({'numero': numero_aluno, 'altura': altura_cm})
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")

    if not dados_alunos:
        print("Nenhum dado de aluno foi inserido.")
        return

    aluno_mais_alto = None
    aluno_mais_baixo = None

    for aluno in dados_alunos:
        if aluno_mais_alto is None or aluno['altura'] > aluno_mais_alto['altura']:
            aluno_mais_alto = aluno
        if aluno_mais_baixo is None or aluno['altura'] < aluno_mais_baixo['altura']:
            aluno_mais_baixo = aluno
    
    print("\n--- Análise de Altura dos Alunos ---")
    print(f"Aluno mais alto: Número {aluno_mais_alto['numero']}, Altura {aluno_mais_alto['altura']:.2f} cm.")
    print(f"Aluno mais baixo: Número {aluno_mais_baixo['numero']}, Altura {aluno_mais_baixo['altura']:.2f} cm.")
