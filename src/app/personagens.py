import random
from app.grafo import Grafo
from app.algoritmos import dijkstra

class Minotauro:
    """
    Representa o personagem Minotauro e sua inteligência artificial no labirinto.

    Esta classe controla a posição, o estado (patrulhando ou perseguindo)
    e as ações do Minotauro a cada rodada, utilizando seu conhecimento completo
    do labirinto para caçarr o prisioneiro.
    """

    def __init__(self, posicao_inicial: int, parametro_percepcao: float, grafo_labirinto: Grafo):

        self.posicao_atual = posicao_inicial
        self.percepcao = parametro_percepcao
        self.grafo = grafo_labirinto
        
        # Atributos para o relatório
        self.em_perseguicao = False
        self.movimento_da_rodada = [] # Guarda o caminho percorrido na rodada atual

        self.caminho_perseguicao_completo = []
        self.posicao_do_prisioneiro_no_inicio_da_perseguicao = None

    def mover(self, prisioneiro: 'Prisioneiro') -> None:
        """
        Executa a lógica de movimento do Minotauro para a rodada atual.
        
        Primeiro calcula a distância até o prisioneiro e determina se deve
        entrar em modo de perseguição. Em seguida, move-se de acordo com
        o estado atual (patrulha ou perseguição).
        """
        # Salva o estado anterior para detectar mudanças de comportamento
        estava_perseguindo = self.em_perseguicao

        # Calcula distâncias e caminhos mínimos usando algoritmo de Dijkstra
        distancias, predecessores = dijkstra(self.grafo, self.posicao_atual)
        self.distancia_ate_prisioneiro = distancias[prisioneiro.posicao_atual]

        # Determina se o minotauro está em estado de percepção
        self._is_em_perseguicao()

        # Gerencia início e fim da perseguição para o relatório
        if self.em_perseguicao and not estava_perseguindo:
            # Iniciou perseguição: registra posição inicial e do prisioneiro
            self.caminho_perseguicao_completo = [self.posicao_atual]
            self.posicao_do_prisioneiro_no_inicio_da_perseguicao = prisioneiro.posicao_atual
        elif not self.em_perseguicao and estava_perseguindo:
            # Terminou perseguição: limpa dados de rastreamento
            self.caminho_perseguicao_completo = []
            self.posicao_do_prisioneiro_no_inicio_da_perseguicao = None

        # Executa movimento baseado no estado atual
        if self.em_perseguicao:
            # Modo perseguição: segue caminho mínimo até o prisioneiro
            caminho_minimo = self._reconstruir_caminho(predecessores, prisioneiro.posicao_atual)
            self._mover_perseguindo(caminho_minimo)
            self.caminho_perseguicao_completo.extend(self.movimento_da_rodada)
        else:
            # Modo patrulha: movimento aleatório
            self._mover_patrulhando()

    def _is_em_perseguicao(self):
        """
        Determina se o Minotauro deve entrar em modo de perseguição
        baseado na distância até o prisioneiro e seu alcance de percepção.
        """
        if self.distancia_ate_prisioneiro <= self.percepcao:
            self.em_perseguicao = True
        else:
            self.em_perseguicao = False

    def _reconstruir_caminho(self, predecessores: list[int], destino: int) -> list[int]:
        """
        Reconstrói o caminho mínimo da posição atual até o destino,
        usando o vetor de predecessores retornado pelo Dijkstra.
        """
        caminho = []
        vertice_atual = destino
        
        # O caminho é impossível se não houver predecessor
        if predecessores[vertice_atual] is None:
            return []

        while vertice_atual is not None:
            caminho.append(vertice_atual)
            if vertice_atual == self.posicao_atual:
                break
            vertice_atual = predecessores[vertice_atual]

        caminho.reverse()
        return caminho

    def _mover_perseguindo(self, caminho: list[int]) -> None:
        """
        Move-se até 2 vértices no caminho mínimo durante a perseguição. 
        """
        self.movimento_da_rodada = []
        if len(caminho) <= 1:
            return # Já está no mesmo vértice ou não há caminho

        # Determina o número de passos a dar (1 ou 2)
        passos_a_dar = min(2, len(caminho) - 1)
        
        # Guarda os vértices do movimento para o relatório. O caminho[0] é a posição atual.
        self.movimento_da_rodada = caminho[1 : passos_a_dar + 1]
        
        # Atualiza a posição atual para o último vértice alcançado na rodada.
        self.posicao_atual = self.movimento_da_rodada[-1]

    def _mover_patrulhando(self) -> None:
        """
        Move-se 1 vértice aleatoriamente quando não está perseguindo.
        A escolha de um vértice adjacente aleatório é uma estratégia de patrulha válida.
        """
        self.movimento_da_rodada = []
        vizinhos = self.grafo.lista_adj.get(self.posicao_atual, [])

        proximo_vertice, _ = random.choice(vizinhos)
        self.posicao_atual = proximo_vertice
        self.movimento_da_rodada = [proximo_vertice]

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
