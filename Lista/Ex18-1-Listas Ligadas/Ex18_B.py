class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    # (Código da implementação anterior...)

    def inverter(self):
        atual = self.primeiro
        anterior = None
        proximo = None
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.primeiro = anterior

    # Restante do código...

# Exemplo de uso:
lista = ListaLigada()
lista.inserir(5)
lista.inserir(10)
lista.inserir(15)

print("Lista original:")
lista.imprimir()  # Saída esperada: 15 -> 10 -> 5 -> None

lista.inverter()

print("Lista invertida:")
lista.imprimir()  # Saída esperada: 5 -> 10 -> 15 -> None
