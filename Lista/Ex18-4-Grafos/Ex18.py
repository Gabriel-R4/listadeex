# Os grafos são estruturas de dados que representam relacionamentos entre entidades. Consistem em vértices (também chamados de nós) e arestas que conectam esses vértices. Essa estrutura é fundamental em muitas aplicações do mundo real, como redes de computadores, rotas em sistemas de transporte, modelagem de relações sociais e muito mais.

# ### Representações de Grafos:

# #### Matriz de Adjacência:
# Uma matriz de adjacência é uma forma de representar grafos onde as linhas e colunas correspondem aos vértices do grafo. Se o vértice i está conectado ao vértice j por uma aresta, o valor na posição (i, j) será 1 (ou o peso da aresta, se houver). Se não estiver conectado, o valor será 0.

# #### Lista de Adjacência:
# Na lista de adjacência, cada vértice do grafo mantém uma lista de seus vizinhos (vértices conectados a ele). Pode ser implementada como uma estrutura de dados como uma lista de listas, um dicionário ou um array de listas ligadas, onde cada elemento da lista representa os vértices adjacentes ao vértice correspondente.

### Exemplo de Implementação:

#### Matriz de Adjacência:

class GrafoMatrizAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso=1):
        self.matriz[origem][destino] = peso
        # Se o grafo é não-direcionado, pode ser necessário adicionar também (destino, origem) com o mesmo peso

    def imprimir_grafo(self):
        for linha in self.matriz:
            print(linha)


#### Lista de Adjacência:

class GrafoListaAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso=1):
        self.lista[origem].append((destino, peso))
        # Se o grafo é não-direcionado, pode ser necessário adicionar também (destino, origem) com o mesmo peso

    def imprimir_grafo(self):
        for i, vizinhos in enumerate(self.lista):
            print(f"Vértice {i}: {vizinhos}")


### Busca em Grafos:

# #### Busca em Profundidade (DFS) e Busca em Largura (BFS):
# São algoritmos para percorrer ou buscar em grafos. A DFS utiliza pilha (ou recursão) e explora o máximo possível por caminho antes de recuar. Já a BFS utiliza fila e explora todos os vizinhos de um vértice antes de avançar.

# Para implementar uma busca em grafos, você pode usar esses algoritmos. Por exemplo, a DFS pode ser implementada de maneira recursiva:

def dfs(grafo, vertice, visitados):
    visitados.add(vertice)
    print(vertice, end=' ')

    for vizinho, _ in grafo.lista[vertice]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)


# Esses são apenas exemplos básicos para ajudar a compreender as estruturas e operações de grafos. As aplicações são vastas, desde sistemas de recomendação até algoritmos de roteamento em redes, dependendo das necessidades específicas do problema.