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