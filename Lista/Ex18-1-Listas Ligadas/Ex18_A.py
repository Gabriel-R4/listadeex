class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.primeiro = None

    def inserir(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def remover(self, valor):
        atual = self.primeiro
        anterior = None
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar(self, valor):
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor, end=' -> ')
            atual = atual.proximo
        print("None")


# Exemplo de uso:
lista = ListaLigada()
lista.inserir(5)
lista.inserir(10)
lista.inserir(15)
lista.imprimir()  # Saída esperada: 15 -> 10 -> 5 -> None

lista.remover(10)
lista.imprimir()  # Saída esperada: 15 -> 5 -> None

print(lista.buscar(5))  # Saída esperada: True
print(lista.buscar(20))  # Saída esperada: False
