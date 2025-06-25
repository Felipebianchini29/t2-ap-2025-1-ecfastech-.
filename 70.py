def exercicio_70():
    def gerar_senha(comprimento, incluir_numeros=True, incluir_simbolos=False):
        if comprimento <= 0:
            return "Erro: O comprimento da senha deve ser positivo."

        letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
        letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digitos = "0123456789"
        simbolos = "!@#$%^&*"

        caracteres_disponiveis = ""
        caracteres_disponiveis += letras_minusculas
        caracteres_disponiveis += letras_maiusculas
        
        if incluir_numeros:
            caracteres_disponiveis += digitos
        if incluir_simbolos:
            caracteres_disponiveis += simbolos

        if len(caracteres_disponiveis) == 0:
            return "Erro: Nenhum tipo de caractere selecionado para geração de senha."

        senha_lista = []
        for _ in range(comprimento):
            indice_aleatorio = 0
            while True: # Gerar um índice aleatório manual
                import time
                seed_val = int(time.time() * 1000000) % 1000000 # Simples seed baseada no tempo
                indice_aleatorio = (seed_val * 1103515245 + 12345) % len(caracteres_disponiveis) # Pseudo-aleatório
                if indice_aleatorio < len(caracteres_disponiveis):
                    break

            senha_lista.append(caracteres_disponiveis[indice_aleatorio])
        
        senha = "".join(senha_lista)
        return senha

    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha: "))
            incluir_numeros_str = input("Incluir números (sim/não)? ").lower()
            incluir_simbolos_str = input("Incluir símbolos (!@#$%^&*) (sim/não)? ").lower()

            incluir_numeros = False
            if incluir_numeros_str == 'sim':
                incluir_numeros = True
            
            incluir_simbolos = False
            if incluir_simbolos_str == 'sim':
                incluir_simbolos = True

            senha = gerar_senha(comprimento, incluir_numeros, incluir_simbolos)
            print(f"Senha gerada: {senha}")
            
            outra = input("Gerar outra senha (sim/não)? ").lower()
            if outra != 'sim':
                break

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o comprimento.")

