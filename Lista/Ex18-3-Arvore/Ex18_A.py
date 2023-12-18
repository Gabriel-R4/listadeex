class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if not no_atual:
            return No(valor)

        if valor < no_atual.valor:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, valor)
        return no_atual

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no_atual, valor):
        if not no_atual:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._remover_recursivo(no_atual.direita, valor)
        else:
            if not no_atual.esquerda:
                return no_atual.direita
            elif not no_atual.direita:
                return no_atual.esquerda

            temp = self._minimo_valor(no_atual.direita)
            no_atual.valor = temp.valor
            no_atual.direita = self._remover_recursivo(no_atual.direita, temp.valor)

        return no_atual

    def _minimo_valor(self, no_atual):
        while no_atual.esquerda:
            no_atual = no_atual.esquerda
        return no_atual

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no_atual, valor):
        if not no_atual or no_atual.valor == valor:
            return no_atual is not None

        if valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)

# Exemplo de uso:
arvore = ArvoreBinariaBusca()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(12)
arvore.inserir(18)

print(arvore.buscar(7))  # Saída esperada: True
print(arvore.buscar(11))  # Saída esperada: False

arvore.remover(5)
print(arvore.buscar(5))  # Saída esperada: False
