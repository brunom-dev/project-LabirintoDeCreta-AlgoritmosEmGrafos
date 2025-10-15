from app.grafo import Grafo

def ler_labirinto(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        num_vertices = int(arquivo.readline().strip())
        num_arestas = int(arquivo.readline().strip())

        labirinto = Grafo(num_vertices)

        # para cada aresta do grafo, obtemos (u,v) e o peso. E adicionamos no grafo
        for _ in range(num_arestas):
            linha = arquivo.readline().strip().split()
            u, v, peso = int(linha[0]), int(linha[1]), int(linha[2])
            labirinto.adicionar_aresta(u, v, peso) 

        entrada_labirinto = int(arquivo.readline().strip())
        saida_labirinto = int(arquivo.readline().strip())
        posicao_minotauro = int(arquivo.readline().strip())
        percepcao_minotauro = int(arquivo.readline().strip())
        tempo_maximo = int(arquivo.readline().strip())

        parametros = {
            "entrada_labirinto": entrada_labirinto,
            "saida_labirinto": saida_labirinto,
            "posicao_minotauro": posicao_minotauro,
            "percepcao_minotauro": percepcao_minotauro,
            "tempo_maximo": tempo_maximo
        }

        return labirinto, parametros


try:
    arquivo_labirinto = "src/labirintos/labirinto.txt"

    grafo_labirinto, parametros_simulacao = ler_labirinto(arquivo_labirinto)

    print("--- Grafo do Labirinto ---")
    print(grafo_labirinto)
    
    print("\n--- Parâmetros da Simulação ---")
    for chave, valor in parametros_simulacao.items():
        print(f"{chave.capitalize()}: {valor}")

except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_labirinto}' não encontrado.")
        print("Por favor, crie o arquivo com os dados do labirinto para testar.")