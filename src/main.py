import time
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
        print("Por favor, crie o arquivo com os dados do labirinto para testar.")