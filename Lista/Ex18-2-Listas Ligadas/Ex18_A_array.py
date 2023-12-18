# Pilha utilizando Arrays:
class PilhaArray:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        return None

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        return None

    def tamanho(self):
        return len(self.items)

# Exemplo de uso:
pilha_array = PilhaArray()
pilha_array.empilhar(1)
pilha_array.empilhar(2)
pilha_array.empilhar(3)

print("Topo da pilha (array):", pilha_array.topo())  # Saída esperada: 3

pilha_array.desempilhar()
print("Topo da pilha após desempilhar (array):", pilha_array.topo())  # Saída esperada: 2
