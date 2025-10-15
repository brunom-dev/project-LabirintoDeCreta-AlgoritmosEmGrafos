class Grafo:
    """
        Classe para representar o labirinto como um grafo ponderado e não direcionado.
    """
    def __init__(self, n):
        """
            Inicializa um grafo
        """
        
        # n: Número de vértices (posições no labirinto).
        self.num_vertices = n

        # adj: dicionario com chave e valor, onde
        # chave: vertice (int)
        # valor: lista de tuplas [ (vizinho, peso), ...] 
        self.lista_adj = {i: [] for i in range(1, n+1)}

    def adicionar_aresta(self, u, v, peso):
        """
            Adiciona uma aresta ponderada entre os vértices u e v.
            Como temos um grafo não direicionado, adicionamos 
            a aresta nos dois sentidos.
        """
        self.lista_adj[u].append(v, peso)
        self.lista_adj[v].append(u, peso)

    def __str__(self):
        """
            Função para imprimir o grafo de forma legivel.
        """
        resultado = ""
        for vertice, vizinhos in self.lista_adj.items():
            resultado += f"Vertice {vertice}: {vizinhos}\n"
        return resultado
    
    