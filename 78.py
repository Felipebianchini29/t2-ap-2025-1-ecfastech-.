def exercicio_78():
    def contar_linhas(nome_arquivo):
        try:
            f = open(nome_arquivo, 'r')
            contagem = 0
            for linha in f:
                contagem += 1
            f.close()
            return contagem
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return 0
        except IOError as e:
            print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
            return 0
    
    nome_arquivo = input("Digite o nome do arquivo para contar as linhas (ex: dados.txt): ")
    num_linhas = contar_linhas(nome_arquivo)
    if num_linhas > 0:
        print(f"O arquivo '{nome_arquivo}' tem {num_linhas} linhas.")
