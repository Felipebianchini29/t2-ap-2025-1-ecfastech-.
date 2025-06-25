def exercicio_82():
    def somar_numeros_arquivo(nome_arquivo):
        soma_total = 0
        try:
            f = open(nome_arquivo, 'r')
            for linha in f:
                linha_limpa = ""
                for char in linha:
                    if char != '\n':
                        linha_limpa += char
                try:
                    num = int(linha_limpa)
                    soma_total += num
                except ValueError:
                    print(f"Aviso: Não foi possível converter a linha '{linha_limpa}' para um número inteiro. Ignorando.")
            f.close()
            return soma_total
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return 0
        except IOError as e:
            print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
            return 0
    
    nome_arquivo = input("Digite o nome do arquivo com números (ex: numeros.txt): ")
    soma_resultado = somar_numeros_arquivo(nome_arquivo)
    print(f"A soma dos números em '{nome_arquivo}' é: {soma_resultado}.")

