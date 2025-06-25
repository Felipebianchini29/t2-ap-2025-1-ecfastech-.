def exercicio_83():
    def copiar_arquivo(origem, destino):
        try:
            f_origem = open(origem, 'r')
            conteudo = ""
            for linha in f_origem:
                conteudo += linha
            f_origem.close()
            
            f_destino = open(destino, 'w')
            f_destino.write(conteudo)
            f_destino.close()
            print(f"Conteúdo copiado com sucesso de '{origem}' para '{destino}'.")
        except FileNotFoundError:
            print(f"Erro: Arquivo de origem '{origem}' não encontrado.")
        except IOError as e:
            print(f"Erro ao copiar arquivo: {e}")

    arquivo_origem = input("Digite o nome do arquivo de origem (ex: dados.txt): ")
    arquivo_destino = input("Digite o nome do arquivo de destino (ex: dados_copia.txt): ")
    
    copiar_arquivo(arquivo_origem, arquivo_destino)

