class ArvoreBinariaBusca:
    # (código da implementação anterior...)

    def calcular_altura(self):
        return self._calcular_altura_recursivo(self.raiz)

    def _calcular_altura_recursivo(self, no_atual):
        if not no_atual:
            return -1  # Definimos a altura de um nó vazio como -1

        altura_esquerda = self._calcular_altura_recursivo(no_atual.esquerda)
        altura_direita = self._calcular_altura_recursivo(no_atual.direita)

        return 1 + max(altura_esquerda, altura_direita)
