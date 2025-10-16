from app.grafo import Grafo
from app.algoritmos import dijkstra

class Minotauro:
    """
    Representa o personagem Minotauro e sua inteligência artificial no labirinto.

    Esta classe controla a posição, o estado (patrulhando ou perseguindo)
    e as ações do Minotauro a cada rodada, utilizando seu conhecimento completo
    do labirinto para caçar o prisioneiro.
    """

    def __init__(self, posicao_inicial: int, parametro_percepcao: float, grafo_labirinto: Grafo):
        """
        Inicializa um novo objeto Minotauro.

        Args:
            posicao_inicial (int): O vértice (posição) inicial do Minotauro no grafo.
            parametro_percepcao (float): A distância máxima (soma dos pesos das arestas)
                                         na qual o Minotauro pode detectar o prisioneiro.
            grafo_labirinto (Grafo): O objeto Grafo que representa o labirinto. O Minotauro
                                     tem conhecimento total dele.
        """
        # --- Atributos de Estado ---
        self.posicao_atual = posicao_inicial
        self.em_perseguicao = False
        self.caminho_perseguicao_atual = [] # Guarda o caminho da rodada atual para o relatório

        # --- Atributos de Configuração ---
        self.percepcao = parametro_percepcao
        self.grafo = grafo_labirinto

class Prisioneiro: 
    """
        Representa o prisioneiro, seu estado e sua lógica de movimento.
    """

    def __init__(self, posicao_inicial):
        self.posicao_atual = posicao_inicial
        # vertices ja visitados.
        self.visitados = {posicao_inicial}
        # pilha para usar como novelo de lâ
        self.caminho_percorrido = [posicao_inicial]
        # historico de movimentos
        self.sequencia_de_movimentos = [posicao_inicial]


    def mover(self, grafo: Grafo):
        vizinhos = grafo.lista_adj[self.posicao_atual]

        for vizinho, peso in vizinhos:
            if vizinho not in self.visitados:
                self.posicao_atual = vizinho
                self.visitados.add(vizinho)
                self.caminho_percorrido.append(vizinho)
                self.sequencia_de_movimentos.append(vizinho)
                return peso # retorna o "tempo" gasto para se mover
            
        if len(self.caminho_percorrido) > 1:
            self.caminho_percorrido.pop()
            posicao_anterior = self.caminho_percorrido[-1]

            peso_retorno = 0
            for vizinho, peso in grafo.lista_adj[self.posicao_atual]:
                if vizinho == posicao_anterior:
                    peso_retorno = peso
                    break
            
            self.posicao_atual = posicao_anterior;
            self.sequencia_de_movimentos.append(self.posicao_atual)
            return peso_retorno
        
        return 0 # Está preso (grafo desconexo) ou ja percorreu todos os vertices.
