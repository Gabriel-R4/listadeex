# Pilha utilizando Listas Ligadas:
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaListaLigada:
    def __init__(self):
        self.topo_pilha = None

    def esta_vazia(self):
        return self.topo_pilha is None

    def empilhar(self, item):
        novo_no = No(item)
        novo_no.proximo = self.topo_pilha
        self.topo_pilha = novo_no

    def desempilhar(self):
        if not self.esta_vazia():
            valor_topo = self.topo_pilha.valor
            self.topo_pilha = self.topo_pilha.proximo
            return valor_topo
        return None

    def topo(self):
        if not self.esta_vazia():
            return self.topo_pilha.valor
        return None

    def tamanho(self):
        tamanho = 0
        atual = self.topo_pilha
        while atual is not None:
            tamanho += 1
            atual = atual.proximo
        return tamanho

# Exemplo de uso:
pilha_lista_ligada = PilhaListaLigada()
pilha_lista_ligada.empilhar(1)
pilha_lista_ligada.empilhar(2)
pilha_lista_ligada.empilhar(3)

print("Topo da pilha (lista ligada):", pilha_lista_ligada.topo())  # Saída esperada: 3

pilha_lista_ligada.desempilhar()
print("Topo da pilha após desempilhar (lista ligada):", pilha_lista_ligada.topo())  # Saída esperada: 2
