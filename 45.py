
def exercicio_45():
    gabarito_prova = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
        6: 'E', 7: 'D', 8: 'C', 9: 'B', 10: 'A'
    }

    alterar_gabarito = input("Deseja inserir um gabarito personalizado (sim/não)? ").lower()
    if alterar_gabarito == 'sim':
        novo_gabarito = {}
        print("Digite a resposta para cada uma das 10 questões (ex: A, B, C, D, E):")
        for i in range(1, 11):
            while True:
                resposta = input(f"Questão {i}: ").upper()
                if resposta in ['A', 'B', 'C', 'D', 'E']:
                    novo_gabarito[i] = resposta
                    break
                else:
                    print("Resposta inválida. Por favor, digite A, B, C, D ou E.")
        gabarito_prova = novo_gabarito
        print("Gabarito atualizado.")

    notas_alunos = []
    total_alunos = 0

    while True:
        total_alunos += 1
        acertos = 0
        print(f"\n--- Prova do Aluno {total_alunos} ---")
        for i in range(1, 11):
            while True:
                resposta_aluno = input(f"Questão {i} (A, B, C, D, E): ").upper()
                if resposta_aluno in ['A', 'B', 'C', 'D', 'E']:
                    if resposta_aluno == gabarito_prova[i]:
                        acertos += 1
                    break
                else:
                    print("Resposta inválida. Por favor, digite A, B, C, D ou E.")
        
        nota = acertos
        notas_alunos.append(nota)
        print(f"Aluno {total_alunos} - Acertos: {acertos}/10, Nota: {nota}.")

        outro_aluno = input("Outro aluno vai utilizar o sistema (sim/não)? ").lower()
        if outro_aluno != 'sim':
            break
    
    if notas_alunos:
        maior_acerto = notas_alunos[0]
        menor_acerto = notas_alunos[0]
        soma_notas = 0
        for nota in notas_alunos:
            if nota > maior_acerto:
                maior_acerto = nota
            if nota < menor_acerto:
                menor_acerto = nota
            soma_notas += nota
        
        media_notas_turma = soma_notas / len(notas_alunos)

        print("\n--- Resumo da Prova ---")
        print(f"Maior Acerto: {maior_acerto}.")
        print(f"Menor Acerto: {menor_acerto}.")
        print(f"Total de Alunos que utilizaram o sistema: {total_alunos}.")
        print(f"A Média das Notas da Turma: {media_notas_turma:.2f}.")
