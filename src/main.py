'''import time
from app.labirinto import ler_labirinto, imprimir_labirinto
from app.personagens import Prisioneiro

try:
    arquivo_labirinto = "src/labirintos/labirinto.txt"

    grafo_labirinto, parametros_simulacao = ler_labirinto(arquivo_labirinto)

    print("\n--- Informações ---")
    for chave, valor in parametros_simulacao.items():
        print(f"{chave.capitalize()}: {valor}")

    pos_prisioneiro_inicial = parametros_simulacao["entrada_labirinto"]
    prisioneiro = Prisioneiro(pos_prisioneiro_inicial)

    pos_minotarauro_inicial = parametros_simulacao["posicao_minotauro"]

    # --- LOOP DE TESTE ---
    for turno_atual in range(1, 5):
        imprimir_labirinto(
            grafo_labirinto, 
            prisioneiro.posicao_atual, 
            pos_minotarauro_inicial, 
            turno_atual
        )
        
        peso_movimento = prisioneiro.mover(grafo_labirinto)
        print(f"Prisioneiro se moveu. Custo do movimento: {peso_movimento}")
        
        time.sleep(2)

    print("\n--- Fim ---")
    print(f"Sequência de movimentos do prisioneiro: {prisioneiro.sequencia_de_movimentos}")
    print("\n")

except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_labirinto}' não encontrado.")
        print("Por favor, crie o arquivo com os dados do labirinto para testar.") '''

tempo_insuficiente = False  # variável que informa se ainda há mantimentos suficiente para se percorrer um caminho
minotauro_morreu = False    # variável que informa se o minotauro está vivo e andando pelo grafo
prisioneiro_caminho = [prisioneiro_vertice] # Adiciona o vértice de entrada no caminho do prisioneiro
minotauro_caminho_perseguicao = []
momento_deteccao = False       # variável que avisa o início da perseguição
encontro_para_batalha = None   # variável que marca se houve o encontro do minotauro com o prisioneiro

# enquanto o prisioneiro ainda tem mantimentos e não chegou na saída
while tempo > 0 and prisioneiro_vertice != saida_vertice:

    # --- Turno do Prisioneiro ----

    # se, na lista de vizinhos, há vizinhos que não foram visitados, escolhe-se um aleatório  
    if vizinhos_nao_visitados:
        # se não há mantimento suficiente para percorrer a aresta o prisioneiro morre no meio do caminho
        if tempo < aresta(prisioneiro_vertice, vizinho_aleatorio):  
            tempo_insuficiente = True
            break
        else:
            tempo -= aresta (prisioneiro_vertice, vizinho_aleatorio)
            prisioneiro_vertice = vizinho_aleatorio
            prisioneiro_caminho.append(prisioneiro_vertice) # guarda o veŕtice percorrido no vetor de caminho

    # se o prisioneiro encontrou um beco sem saída, retorna um vértice    
    else:
        # se não há mantimento suficiente para percorrer a aresta o prisioneiro morre no meio do caminho
        if tempo < aresta(prisioneiro_vertice, vizinho_anterior):  
            tempo_insuficiente = True
            break
        else:
            tempo -= aresta (prisioneiro_vertice, vertice_anterior)
            prisioneiro_vertice = vertice_anterior
            prisioneiro_caminho.append(prisioneiro_vertice) # guarda o veŕtice percorrido no vetor de caminho

    # se o prisioneiro já encontrou a saída, não é preciso executar o turno do minotauro
    if prisioneiro_vertice == saida_vertice:
        break

    # --- Turno do Minotauro -----

    # caso o minotauro morra na batalha com o prisioneiro, apenas o prisioneiro permanece se movendo
    if not minotauro_morreu:
        
        # Utiliza o Dijkstra para encontrar os caminhos mínimos e seus custos
        custos, predecessores = Dijkstra (Grafo, minotauro_vertice)

        '''se o custo para ir do minotauro ao prisioneiro é menor ou igual que a distância de percepção do minotauro,
        então o prisioneiro entrou no raio de detecção do minotauro e a perseguição começa '''
        if (custos[prisioneiro_vertice] <= percepcao_minotauro):

            # guarda as posições do prisioneiro e minotauro no início da perseguição
            if not momento_deteccao:
                momento_deteccao = True
                prisioneiro_inicio_perseguicao = prisioneiro_vertice
                minotauro_inicio_perseguicao = minotauro_vertice
            
            # caminho traçado pelo minotauro durante o modo de perseguição
            minotauro_caminho_perseguicao = [minotauro_vertice]

            # Construção do caminho do minotauro ao prisioneiro
            caminho_temp = []
            vertice_atual = prisioneiro_vertice

            # Construção do caminho do prisioneiro ao minotauro 
            while vertice_atual is not None and vertice_atual != minotauro_vertice:
                caminho_temp.append(vertice_atual)
                vertice_atual = predecessores[vertice_atual]    
            caminho_temp.append(minotauro_vertice)
            caminho_perseguicao = caminho_temp[::-1] # Inverte para ter a ordem correta

            ''' se o minotauro estiver a 1 vértice de distância do prisioneiro, basta que se percorra 1 vértice
            caso contrário, o minotauro em fúria percorre os dois vértices, por padrão '''
            if len(caminho_perseguicao) > 2:
                # adiciona os 2 vértices percorridos ao histórico caminho do minotauro
                minotauro_caminho_perseguicao.append(caminho_da_perseguicao[1])
                minotauro_caminho_perseguicao.append(caminho_da_perseguicao[2])
                # anda 2 vértices
                minotauro_vertice = caminho_perseguicao[2]
            elif len(caminho_perseguicao) > 1:
                # adiciona o vértice ao histórico do caminho do minotauro
                minotauro_caminho_perseguicao.append(caminho_da_perseguicao[1])
                # anda apenas 1 vértice
                minotauro_vertice = caminho_perseguicao[1]
            
            # se o minotauro alcançou o prisioneiro, ocorre a batalha
            if (minotauro_vertice == prisioneiro_vertice):
                encontro_para_batalha = minotauro_vertice  # guarda o momento que o minotauro alcança o prisioneiro
                
                # momento da batalha
                resultado = random.randint(1, 100)
                if resultado == 7:        # número arbitrário para representar a possibilidade de 1% 
                    prisioneiro_sobreviveu = True
                    minotauro_morreu = True
                else: 
                    prisioneiro_sobreviveu = False
                    break
        else:
            minotauro_vertice = vizinho_aleatorio_minotauro
            momento_deteccao = False            # Reseta a detecção se o prisioneiro saiu do raio
            minotauro_caminho_perseguicao = []  # Reseta também o caminho

# ---- Relatório Final -----

'''Possibilidades de término do jogo:
1. O prisioneiro se salvou (o mantimento foi suficiente para se chegar na saída)
2. Os mantimentos acabaram e o prisioneiro morreu
3. O prisioneiro foi morto pelo minotauro '''
if prisioneiro_vertice == saida_vertice:
    print(f"O prisioneiro conseguiu sair do labirinto!")
    print(f"Tempo restante até acabar os mantimentos: {tempo}")
elif tempo_insuficiente: 
    print(f"O prisioneiro morreu de fome!")
    print(f"Infelizmente o tempo restante {tempo} foi insuficiente para chegar na saída")
elif not prisioneiro_sobreviveu:
    print(f"O prisioneiro morreu em batalha com o minotauro")
    print(f"Tempo restante até acabar os mantimentos: {tempo}")
    
#imprime caminho do prisioneiro
print (f"Sequência de vértices do caminho percorrido pelo prisioneiro: {' -> '.join(map(str, prisioneiro_caminho))}")

#se houve perseguição    
if momento_deteccao:
    # imprime o momento de detecção do prisioneiro pelo minotauro
    print(f"Início da perseguição: posição do minotauro - {minotauro_inicio_perseguicao} ; posição do prisioneiro - {prisioneiro_inicio_perseguicao}")
    # se houve a batalha, fornece a localização
    if encontro_para_batalha is not None:
        print(f"Minotauro encontra o prisioneiro no vértice - v{encontro_para_batalha}")
    else:
        print(f"O minotauro não alcançou o prisioneiro durante a perseguição")
    # imprime caminho do minotauro
    print (f"Caminho percorrido pelo Minotauro durante a perseguição: {' -> '.join(map(str, minotauro_caminho_perseguicao))}")
else: 
    print(f"O prisioneiro não foi detectado pelo minotauro")

   

