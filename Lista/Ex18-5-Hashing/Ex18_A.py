# Hashing é uma técnica utilizada em ciência da computação para mapear dados de tamanho variável para dados de tamanho fixo. Envolve a utilização de uma função hash que transforma as chaves em um índice que aponta para um local específico na estrutura de dados, geralmente uma tabela de dispersão (hash table).

# ### Estrutura de Dados Hash Table:

# Uma hash table é uma estrutura de dados que armazena dados na forma de pares chave-valor. Consiste em um array (ou vetor) onde cada elemento é chamado de "bucket" (ou slot) e pode armazenar um ou mais pares chave-valor. A função hash é responsável por calcular o índice de cada chave, permitindo acesso rápido aos dados.

# ### Funcionamento e Aplicações:

# - **Rapidez de Acesso:** As hash tables são eficientes para busca, inserção e remoção de dados, desde que a função hash distribua uniformemente os elementos na tabela.
  
# - **Armazenamento e Recuperação Rápida:** São usadas em bancos de dados, caches de sistemas, linguagens de programação para implementar dicionários e conjuntos, entre outras aplicações.

# - **Evitar Colisões:** Uma questão importante nas hash tables é o tratamento de colisões, quando duas chaves diferentes resultam no mesmo índice. Técnicas comuns para lidar com colisões incluem encadeamento separado (cada bucket é uma lista ligada) e resolução de colisão por sondagem (procurando por outro slot disponível).

### Exemplo de Implementação:

class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.table = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def adicionar(self, chave, valor):
        indice = self._hash(chave)
        for par in self.table[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.table[indice].append([chave, valor])

    def obter(self, chave):
        indice = self._hash(chave)
        for par in self.table[indice]:
            if par[0] == chave:
                return par[1]
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for i, par in enumerate(self.table[indice]):
            if par[0] == chave:
                del self.table[indice][i]
                return