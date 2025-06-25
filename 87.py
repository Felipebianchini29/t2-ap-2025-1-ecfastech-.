def exercicio_87():
    def adicionar_numero_linha(nome_arquivo_origem, nome_arquivo_destino):
        try:
            f_origem = open(nome_arquivo_origem, 'r')
            f_destino = open(nome_arquivo_destino, 'w')
            
            numero_linha = 1
            for linha in f_origem:
                f_destino.write(f"{numero_linha} {linha}")
                numero_linha += 1
            
            f_origem.close()
            f_destino.close()
            print(f"Números de linha adicionados com sucesso de '{nome_arquivo_origem}' para '{nome_arquivo_destino}'.")
        except FileNotFoundError:
            print(f"Erro: Arquivo de origem '{nome_arquivo_origem}' não encontrado.")
        except IOError as e:
            print(f"Erro ao processar arquivos: {e}")

    arquivo_origem = input("Digite o nome do arquivo de origem (ex: dados.txt): ")
    arquivo_destino = input("Digite o nome do arquivo de destino para linhas numeradas: ")
    
    adicionar_numero_linha(arquivo_origem, arquivo_destino)