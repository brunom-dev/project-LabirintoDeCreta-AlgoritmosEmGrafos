from app.grafo import Grafo

def floyd_warshall(grafo: Grafo):
    """
        Algoritmo de Floyd-Warshall para encontrar as distâncias mínimas
        entre todos os pares de vértices em um grafo.

        parametro: recebe um objeto da classe Grafo
        retorno: Duas matrizes: matriz de distancias (distancias) e matriz de predecessores (pai)
    """

    n = grafo.num_vertices
    infinito = float("inf")

    distancias = [[infinito for _ in range(n+1)] for _ in range(n+1)];
    pai = [[None for _ in range(n+1)] for _ in range(n+1)];

    for i in range(1, n+1):
        distancias[i][i] = 0; # A distância de um vértice para ele mesmo é 0.
        pai[i][i] = i; # O predecessor de um vértice para si mesmo é ele próprio.


    # Preenche as matrizes com as arestas diretas do grafo.
    for u, vizinhos in grafo.lista_adj.items():
        for v, peso in vizinhos:
            distancias[u][v] = peso;
            pai[u][v] = u; # No caminho direto u->v, o predecessor de v é u.
    

    # Para cada vértice k, verifica se ele pode ser um intermediário
    # para encurtar o caminho entre i e j.
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if ((distancias[i][k] + distancias[k][j]) < distancias[i][j]):
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
                    pai[i][j] = pai[k][j]
    
    return distancias, pai

