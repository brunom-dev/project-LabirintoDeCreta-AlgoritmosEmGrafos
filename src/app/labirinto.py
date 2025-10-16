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

def imprimir_labirinto(grafo: Grafo, posicao_prisioneiro, posicao_minotauro, turno=0):
    print(f"\n--- Labirinto (Turno {turno}) ---")
    
    for vertice, vizinhos in sorted(grafo.lista_adj.items()):
        # Monta a string com os vizinhos e pesos
        vizinhos_str = "".join([f" -> ({v}, peso {p})" for v, p in vizinhos])
        
        linha = f"Vértice {vertice}:{vizinhos_str}"
        
        # Indica em qual posicao os personagens estão.
        indicadores = []
        if vertice == posicao_prisioneiro:  
            indicadores.append("PRISIONEIRO")
        if vertice == posicao_minotauro:
            indicadores.append("MINOTAURO")
        
        if indicadores:
            linha += f"  <-- ({', '.join(indicadores)})"
            
        print(linha)
