import heapq

class FilaPrioridade:
    def __init__(self):
        self._fila = []
        self._contador = 0  # Usado para resolver empates em prioridade

    def inserir(self, item, prioridade):
        heapq.heappush(self._fila, (-prioridade, self._contador, item))
        self._contador += 1

    def remover(self):
        return heapq.heappop(self._fila)[-1]

    def tamanho(self):
        return len(self._fila)

    def esta_vazia(self):
        return len(self._fila) == 0

# Exemplo de uso:
fila_prioridade = FilaPrioridade()
fila_prioridade.inserir('Tarefa 1', 3)
fila_prioridade.inserir('Tarefa 2', 5)
fila_prioridade.inserir('Tarefa 3', 1)

while not fila_prioridade.esta_vazia():
    print(fila_prioridade.remover())
# Saída esperada: Tarefa 2, Tarefa 1, Tarefa 3 (removidas na ordem de prioridade)
