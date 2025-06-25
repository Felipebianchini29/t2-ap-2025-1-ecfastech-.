def exercicio_79():
    def ler_e_imprimir(nome_arquivo):
        try:
            f = open(nome_arquivo, 'r')
            print(f"\n--- Conteúdo de '{nome_arquivo}' ---")
            for linha in f:
                print(linha, end='')
            print(f"--- Fim de '{nome_arquivo}' ---")
            f.close()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        except IOError as e:
            print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
    
    nome_arquivo = input("Digite o nome do arquivo para ler e imprimir (ex: dados.txt): ")
    ler_e_imprimir(nome_arquivo)