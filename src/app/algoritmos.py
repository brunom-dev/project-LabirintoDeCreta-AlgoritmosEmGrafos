from app.grafo import Grafo
import heapq

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

def dijkstra(grafo: Grafo, origem: int):
    """
    Algoritmo de Dijkstra otimizado com heap de prioridade (Min-Heap).
    Encontra o caminho de menor custo (distância) da 'origem' para todos os outros vértices.
    """
    
    # 1. Inicialização de Estruturas
    n = grafo.num_vertices
    infinito = float("inf")

    # Arrays de resultados: Distância inicial infinita e pai (predecessor) nulo
    distancias = [infinito] * (n + 1)
    pai = [None] * (n + 1)
    
    # Define a distância da origem para ela mesma como 0
    distancias[origem] = 0
    pai[origem] = origem

    # Min-Heap: Armazena (distancia, vertice). A menor distância tem prioridade.
    heap = [(0, origem)]
    
    # Controle de vértices processados (otimização para evitar re-processamento)
    visitado = [False] * (n + 1)

    # 2. Laço Principal de Dijkstra
    while heap:
        # Extrai o vértice 'u' com a menor distância atual (propriedade do Min-Heap)
        dist_u, u = heapq.heappop(heap)
        
        # Se 'u' já foi extraído e processado anteriormente, ignora esta cópia
        if visitado[u]:
            continue
            
        # Marca 'u' como processado, garantindo que sua distância final foi determinada
        visitado[u] = True

        # 3. Relaxamento das Arestas
        # Itera sobre todos os vizinhos 'v' de 'u'
        for v, peso in grafo.lista_adj.get(u, []):
            nova_dist = dist_u + peso
            
            # Teste de Relaxamento: Se encontrou um caminho mais curto para 'v' através de 'u'
            if nova_dist < distancias[v]:
                # Atualiza a menor distância e o predecessor
                distancias[v] = nova_dist
                pai[v] = u
                
                # Insere 'v' no heap com sua nova e menor distância
                # O heap garante que 'v' será processado na ordem correta
                heapq.heappush(heap, (nova_dist, v))

    return distancias, pai