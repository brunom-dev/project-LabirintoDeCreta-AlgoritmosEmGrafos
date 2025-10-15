# Projeto: Labirinto de Creta

Este projeto é uma implementação para a disciplina de **Algoritmos em Grafos** da Universidade Federal do Cariri (UFCA). O objetivo é simular a dinâmica de um prisioneiro tentando escapar de um labirinto enquanto é caçado pelo Minotauro. O labirinto é modelado como um grafo ponderado, e a simulação envolve algoritmos de busca e de caminho mínimo.

## Como Executar

1.  **Pré-requisitos:**
    * Python 3.x

2.  **Execução:**
    * Clone este repositório.
    * Execute o arquivo principal do simulador terminal. Certifique-se de que o arquivo de entrada do labirinto esteja no diretório de labirintos (ex: `labirintos/labirinto.txt`) ou forneça o caminho correto. 
    <br>
    
    ```
    python nome_do_arquivo_principal.py
    ```

### Formato do Arquivo de Entrada

O programa espera um arquivo de texto com a seguinte estrutura:
1.  Número de vértices $|V|$
2.  Número de arestas $|E|$
3.  Lista de $|E|$ arestas no formato `u v peso`
4.  Vértice de entrada
5.  Vértice de saída
6.  Posição inicial do Minotauro
7.  Parâmetro de percepção do Minotauro $p(G)$
8.  Tempo máximo de sobrevivência $\tau(G)$

## Equipe

* **[Andrey Bernardo Rocha (Github)](https://github.com/rochaandrey)**
* **[Bruno da Silva Macedo (Github)](https://github.com/brunom-dev)**
* **[Marcus Vinicius Oliveira Ventura (Github)](https://github.com/MarcusVentura14)**

## Professor

* **[Carlos Vinicius Gomes Costa Lima (Email Institucional)](mailto:vinicius.lima@ufca.edu.br)**
