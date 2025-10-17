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
        if random.randint(1,100) == 1:
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
            if random.randint(1, 100) == 1:
                print("\nMILAGRE: Prisioneiro venceu a batalha!")
                minotauro_morreu = True
                minotauro.posicao_atual = -1
            else:
                print("\nDERROTA: Prisioneiro foi capturado pelo Minotauro!")
                status_final = "CAPTURA"
                break


def gerar_relatorio_final(status_final, prisioneiro, minotauro, tempo_restante):
    """
    Imprime o relatório completo 
    """

    print("\n" + "="*40)
    print("--- RELATÓRIO FINAL DA SIMULAÇÃO ---")
    print("="*40)

    # 1. Imprime o resultado principal (Causa do Fim do Jogo)
    if status_final == "VITORIA":
        print("\n[★] Resultado: O prisioneiro escapou do labirinto!")
    elif status_final == "FOME":
        print("\n[☹] Resultado: O prisioneiro morreu de fome.")
    elif status_final == "CAPTURA":
        print("\n[☠] Resultado: O prisioneiro foi capturado e morto pelo Minotauro.")
    elif status_final == "VITORIA_BATALHA":
        print("\n[⚔] Resultado: Em um ato heroico, o prisioneiro venceu o Minotauro em batalha!")
    
    # Imprime o tempo restante de comida 
    print(f"Tempo restante de comida: {max(0, tempo_restante)}")

    print("\n" + "-"*40)

    # Imprime o caminho do Prisioneiro
    print("--- Detalhes do Prisioneiro ---")
    caminho_p_str = ' -> '.join(map(str, prisioneiro.sequencia_de_movimentos))
    print(f"Sequência de movimentos: {caminho_p_str}")
    
    print("\n" + "-"*40)
    
    # 3. Imprime informações sobre a perseguição, usando os atributos do Minotauro
    print("--- Detalhes da Caçada do Minotauro ---")
    
    # Verifica se a perseguição ocorreu usando o atributo que guarda a posição inicial do prisioneiro
    if minotauro.posicao_do_prisioneiro_no_inicio_da_perseguicao is not None:
        # Pega a posição do minotauro no início da perseguição (primeiro item do caminho)
        pos_m_inicio_perseguicao = minotauro.caminho_perseguicao_completo[0]
        pos_p_inicio_perseguicao = minotauro.posicao_do_prisioneiro_no_inicio_da_perseguicao

        print("Status da Perseguição: O prisioneiro foi detectado!") 
        print(f"Momento da detecção:") 
        print(f"  - Posição do Minotauro: {pos_m_inicio_perseguicao}")
        print(f"  - Posição do Prisioneiro: {pos_p_inicio_perseguicao}")
        
        # Imprime o caminho completo percorrido pelo Minotauro DURANTE a perseguição 
        caminho_m_str = ' -> '.join(map(str, minotauro.caminho_perseguicao_completo))
        print(f"Caminho do Minotauro durante a perseguição: {caminho_m_str}")

        if status_final == "CAPTURA":
            print(f"Momento da captura: O Minotauro alcançou o prisioneiro no vértice {minotauro.posicao_atual}.")

    else:
        print("Status da Perseguição: O prisioneiro nunca foi detectado pelo Minotauro.")

    print("="*40)

gerar_relatorio_final(status_final,prisioneiro, minotauro, tempo_restante)
