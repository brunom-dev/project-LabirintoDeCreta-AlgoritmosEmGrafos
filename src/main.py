import random
from app.labirinto import ler_labirinto, imprimir_labirinto
from app.personagens import Prisioneiro, Minotauro

labirinto, parametros = ler_labirinto("src/labirintos/labirinto.txt")

print("\n--- Informações ---")
for chave, valor in parametros.items():
    print(f"{chave.capitalize()}: {valor}")


prisioneiro = Prisioneiro(parametros["entrada_labirinto"])
minotauro = Minotauro(parametros["posicao_minotauro"], parametros["percepcao_minotauro"], labirinto)

tempo_restante = parametros["tempo_maximo"] 
turno = 0

minotauro_morreu = False;
status_final = ""

while True:
    turno += 1
    imprimir_labirinto(labirinto, prisioneiro.posicao_atual, minotauro.posicao_atual, turno)
    print("\n")

    # --- Turno do Prisioneiro ---

    peso_movimento_prisioneiro = prisioneiro.mover(labirinto)
    tempo_restante -= peso_movimento_prisioneiro

    if not minotauro_morreu: 
        print("(Prisioneiro se moveu)")
        imprimir_labirinto(labirinto, prisioneiro.posicao_atual, minotauro.posicao_atual, turno)

    if (tempo_restante == 0) and (prisioneiro.posicao_atual == parametros["saida_labirinto"]):
        print("\nVITÓRIA: Prisioneiro encontrou a saída POR POUCO!")
        status_final = "VITORIA"
        break

    if tempo_restante <= 0:
        print("\nDERROTA: Prisioneiro morreu de fome!")
        status_final = "FOME"
        break

    if prisioneiro.posicao_atual == parametros["saida_labirinto"]:
        print("\nVITÓRIA: Prisioneiro encontrou a saída!")
        status_final = "VITORIA"
        break


    if prisioneiro.posicao_atual == minotauro.posicao_atual:
        # 1% de chance de vencer o minotauro
        if random.randint(1,1) == 1:
            print("\nMILAGRE: Prisioneiro venceu a batalha")
            minotauro_morreu = True
            minotauro.posicao_atual = -1
        else:
            print("\nDERROTA: Prisioneiro foi capturado pelo Minotauro!")
            status_final = "CAPTURA"
            break


    # --- Turno do Minotauro ---  

    if not minotauro_morreu:

        minotauro.mover(prisioneiro)

        print("\n")
        print("(Minotauro se moveu) ")
        imprimir_labirinto(labirinto, prisioneiro.posicao_atual, minotauro.posicao_atual, turno)

        if minotauro.posicao_atual == prisioneiro.posicao_atual:
            # Lógica da batalha novamente
            if random.randint(1, 1) == 1:
                print("\nMILAGRE: Prisioneiro venceu a batalha!")
                minotauro_morreu = True
                minotauro.posicao_atual = -1
            else:
                print("\nDERROTA: Prisioneiro foi capturado pelo Minotauro!")
                status_final = "CAPTURA"
                break


def gerar_relatorio_final(status_final, prisioneiro, minotauro, tempo_restante, params):
    """
    Imprime o relatório completo.
    """
    print("\n------------------------------------")
    print(" RELATÓRIO FINAL ")
    print("------------------------------------")

    # 1. Imprime o resultado principal (Causa do Fim do Jogo)
    if status_final == "VITORIA":
        print("Resultado: O prisioneiro escapou do labirinto!")
        print(f"Tempo restante de comida: {tempo_restante}")
    elif status_final == "FOME":
        print("Resultado: O prisioneiro morreu de fome.")
        print("O tempo de comida acabou antes que a saída fosse encontrada.")
    elif status_final == "CAPTURA":
        print("Resultado: O prisioneiro foi capturado e morto pelo Minotauro.")
        print(f"Tempo restante de comida no momento da captura: {tempo_restante}")
    
    print("---")

    # 2. Imprime o caminho do Prisioneiro (acessando o atributo do objeto)
    caminho_p_str = ' -> '.join(map(str, prisioneiro.sequencia_de_movimentos))
    print(f"Sequência de movimentos do Prisioneiro: {caminho_p_str}")
    
    print("---")

    # 3. Imprime informações sobre a perseguição (acessando os atributos do Minotauro)
    # Para isso, precisaríamos adicionar um atributo `historico_perseguicao` no Minotauro
    # ou usar as informações que ele já tem.
    
    # Exemplo (supondo que o objeto Minotauro guarde essa informação):
    if True: # Um novo atributo que seria setado para True
        print("Status da Perseguição: O prisioneiro foi detectado.")
        # ... imprimiria o caminho da perseguição do Minotauro ...
    else:
        print("Status da Perseguição: O prisioneiro nunca foi detectado.")
        
    print("------------------------------------")

gerar_relatorio_final(status_final,prisioneiro, minotauro, tempo_restante, parametros)


# -----------------------------------------------------------------------


# tempo_insuficiente = False  # variável que informa se ainda há mantimentos suficiente para se percorrer um caminho
# minotauro_morreu = False    # variável que informa se o minotauro está vivo e andando pelo grafo
# prisioneiro_caminho = [prisioneiro_vertice] # Adiciona o vértice de entrada no caminho do prisioneiro
# minotauro_caminho_perseguicao = []
# momento_deteccao = False   # variável que avisa o início da perseguição
# encontro_para_batalha = None   # variável que marca se houve o encontro do minotauro com o prisioneiro

# # enquanto o prisioneiro ainda tem mantimentos e não chegou na saída
# while tempo > 0 and prisioneiro_vertice != saida_vertice:

#     # --- Turno do Prisioneiro ----

#     # se, na lista de vizinhos, há vizinhos que não foram visitados, escolhe-se um aleatório  
#     if vizinhos_nao_visitados:
#         # se não há mantimento suficiente para percorrer a aresta o prisioneiro morre no meio do caminho
#         if tempo < aresta(prisioneiro_vertice, vizinho_aleatorio):  
#             tempo_insuficiente = True
#             break
#         else:
#             tempo -= aresta (prisioneiro_vertice, vizinho_aleatorio)
#             prisioneiro_vertice = vizinho_aleatorio
#             prisioneiro_caminho.append(prisioneiro_vertice) # guarda o veŕtice percorrido no vetor de caminho

#     # se o prisioneiro encontrou um beco sem saída, retorna um vértice    
#     else:
#         # se não há mantimento suficiente para percorrer a aresta o prisioneiro morre no meio do caminho
#         if tempo < aresta(prisioneiro_vertice, vizinho_anterior):  
#             tempo_insuficiente = True
#             break
#         else:
#             tempo -= aresta (prisioneiro_vertice, vertice_anterior)
#             prisioneiro_vertice = vertice_anterior
#             prisioneiro_caminho.append(prisioneiro_vertice) # guarda o veŕtice percorrido no vetor de caminho

#     # se o prisioneiro já encontrou a saída, não é preciso executar o turno do minotauro
#     if prisioneiro_vertice == saida_vertice:
#         break

#     # --- Turno do Minotauro -----

#     # caso o minotauro morra na batalha com o prisioneiro, apenas o prisioneiro permanece se movendo
#     if not minotauro_morreu:
        
#         # Utiliza o Dijkstra para encontrar os caminhos mínimos e seus custos
#         custos, predecessores = Dijkstra (Grafo, minotauro_vertice)

#         '''se o custo para ir do minotauro ao prisioneiro é menor ou igual que a distância de percepção do minotauro,
#         então o prisioneiro entrou no raio de detecção do minotauro e a perseguição começa '''
#         if (custos[prisioneiro_vertice] <= percepcao_minotauro):

#             # guarda as posições do prisioneiro e minotauro no início da perseguição
#             if not momento_deteccao:
#                 momento_deteccao = True
#                 prisioneiro_inicio_perseguicao = prisioneiro_vertice
#                 minotauro_inicio_perseguicao = minotauro_vertice
            
#             # caminho traçado pelo minotauro durante o modo de perseguição
#             minotauro_caminho_perseguicao = [minotauro_vertice]

#             # Construção do caminho do minotauro ao prisioneiro
#             caminho_temp = []
#             vertice_atual = prisioneiro_vertice

#             # Construção do caminho do prisioneiro ao minotauro 
#             while vertice_atual is not None and vertice_atual != minotauro_vertice:
#                 caminho_temp.append(vertice_atual)
#                 vertice_atual = predecessores[vertice_atual]    
#             caminho_temp.append(minotauro_vertice)
#             caminho_perseguicao = caminho_temp[::-1] # Inverte para ter a ordem correta

#             ''' se o minotauro estiver a 1 vértice de distância do prisioneiro, basta que se percorra 1 vértice
#             caso contrário, o minotauro em fúria percorre os dois vértices, por padrão '''
#             if len(caminho_perseguicao) > 2:
#                 # adiciona os 2 vértices percorridos ao histórico caminho do minotauro
#                 minotauro_caminho_perseguicao.append(caminho_da_perseguicao[1])
#                 minotauro_caminho_perseguicao.append(caminho_da_perseguicao[2])
#                 # anda 2 vértices
#                 minotauro_vertice = caminho_perseguicao[2]
#             elif len(caminho_perseguicao) > 1:
#                 # adiciona o vértice ao histórico do caminho do minotauro
#                 minotauro_caminho_perseguicao.append(caminho_da_perseguicao[1])
#                 # anda apenas 1 vértice
#                 minotauro_vertice = caminho_perseguicao[1]
            
#             # se o minotauro alcançou o prisioneiro, ocorre a batalha
#             if (minotauro_vertice == prisioneiro_vertice):
#                 encontro_para_batalha = minotauro_vertice  # guarda o momento que o minotauro alcança o prisioneiro
                
#                 # momento da batalha
#                 resultado = random.randint(1, 100)
#                 if resultado == 7:        # número arbitrário para representar a possibilidade de 1% 
#                     prisioneiro_sobreviveu = True
#                     minotauro_morreu = True
#                 else: 
#                     prisioneiro_sobreviveu = False
#                     break
#         else:
#             minotauro_vertice = vizinho_aleatorio_minotauro
#             momento_deteccao = False            # Reseta a detecção se o prisioneiro saiu do raio
#             minotauro_caminho_perseguicao = []  # Reseta também o caminho

# # ---- Relatório Final -----

# '''Possibilidades de término do jogo:
# 1. O prisioneiro se salvou (o mantimento foi suficiente para se chegar na saída)
# 2. Os mantimentos acabaram e o prisioneiro morreu
# 3. O prisioneiro foi morto pelo minotauro '''
# if prisioneiro_vertice == saida_vertice:
#     print(f"O prisioneiro conseguiu sair do labirinto!")
#     print(f"Tempo restante até acabar os mantimentos: {tempo}")
# elif tempo_insuficiente: 
#     print(f"O prisioneiro morreu de fome!")
#     print(f"Infelizmente o tempo restante {tempo} foi insuficiente para chegar na saída")
# elif not prisioneiro_sobreviveu:
#     print(f"O prisioneiro morreu em batalha com o minotauro")
#     print(f"Tempo restante até acabar os mantimentos: {tempo}")
    
# #imprime caminho do prisioneiro
# print (f"Sequência de vértices do caminho percorrido pelo prisioneiro: {' -> '.join(map(str, prisioneiro_caminho))}")

# #se houve perseguição    
# if momento_deteccao:
#     # imprime o momento de detecção do prisioneiro pelo minotauro
#     print(f"Início da perseguição: posição do minotauro - {minotauro_inicio_perseguicao} ; posição do prisioneiro - {prisioneiro_inicio_perseguicao}")
#     # se houve a batalha, fornece a localização
#     if encontro_para_batalha is not None:
#         print(f"Minotauro encontra o prisioneiro no vértice - v{encontro_para_batalha}")
#     else:
#         print(f"O minotauro não alcançou o prisioneiro durante a perseguição")
#     # imprime caminho do minotauro
#     print (f"Caminho percorrido pelo Minotauro durante a perseguição: {' -> '.join(map(str, minotauro_caminho_perseguicao))}")
# else: 
#     print(f"O prisioneiro não foi detectado pelo minotauro")

   

