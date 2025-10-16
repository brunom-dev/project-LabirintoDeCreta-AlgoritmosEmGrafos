from app.labirinto import ler_labirinto, imprimir_labirinto

try:
    arquivo_labirinto = "src/labirintos/labirinto.txt"

    grafo_labirinto, parametros_simulacao = ler_labirinto(arquivo_labirinto)

    print("\n--- Informações ---")
    for chave, valor in parametros_simulacao.items():
        print(f"{chave.capitalize()}: {valor}")

    pos_prisioneiro_inicial = parametros_simulacao["entrada_labirinto"]
    pos_minotarauro_inicial = parametros_simulacao["posicao_minotauro"]

    imprimir_labirinto(grafo_labirinto, pos_prisioneiro_inicial, pos_minotarauro_inicial, 0)
    print("\n")

except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_labirinto}' não encontrado.")
        print("Por favor, crie o arquivo com os dados do labirinto para testar.")