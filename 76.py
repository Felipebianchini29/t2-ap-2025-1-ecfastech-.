def exercicio_76():
    def desenhar_triangulo(altura, tipo):
        if not isinstance(altura, int) or altura <= 0:
            print("Erro: A altura deve ser um número inteiro positivo.")
            return
        
        if tipo not in ['esquerda', 'direita', 'centralizado']:
            print("Erro: Tipo inválido. Escolha 'esquerda', 'direita' ou 'centralizado'.")
            return
        
        print(f"\n--- Triângulo Alinhado à {tipo.capitalize()} (Altura: {altura}) ---")
        for i in range(1, altura + 1):
            asteriscos_lista = []
            for _ in range(i):
                asteriscos_lista.append("*")
            asteriscos = "".join(asteriscos_lista)

            if tipo == 'esquerda':
                print(asteriscos)
            elif tipo == 'direita':
                espacos_faltantes = altura - i
                linha_construida = []
                for _ in range(espacos_faltantes):
                    linha_construida.append(" ")
                for char_ast in asteriscos:
                    linha_construida.append(char_ast)
                print("".join(linha_construida))
            elif tipo == 'centralizado':
                largura_maxima = 2 * altura - 1
                espacos_total = largura_maxima - len(asteriscos)
                espacos_esquerda = espacos_total // 2
                
                linha_construida = []
                for _ in range(espacos_esquerda):
                    linha_construida.append(" ")
                for char_ast in asteriscos:
                    linha_construida.append(char_ast)
                
                # Para centralização, pode haver um espaço extra à direita se a largura_maxima for ímpar e len(asteriscos) for par
                # ou vice-versa. Simplesmente preenche o resto com espaços.
                for _ in range(largura_maxima - len("".join(linha_construida))):
                    linha_construida.append(" ")
                
                print("".join(linha_construida))

    while True:
        try:
            altura = int(input("Digite a altura do triângulo (inteiro positivo): "))
            tipo_alinhamento = input("Digite o tipo de alinhamento ('esquerda', 'direita', 'centralizado'): ").lower()
            
            desenhar_triangulo(altura, tipo_alinhamento)
            
            outro_triangulo = input("Desenhar outro triângulo? (sim/não): ").lower()
            if outro_triangulo != 'sim':
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a altura.")
