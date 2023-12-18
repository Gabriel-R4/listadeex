# Percurso em Ordem (inorder traversal):

class ArvoreBinariaBusca:
    # (código da implementação anterior...)

    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, no_atual):
        if no_atual:
            self._percorrer_em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.valor, end=' ')
            self._percorrer_em_ordem_recursivo(no_atual.direita)

# Percurso Pré-Ordem (preorder traversal):

class ArvoreBinariaBusca:
    # (código da implementação anterior...)

    def percorrer_pre_ordem(self):
        self._percorrer_pre_ordem_recursivo(self.raiz)

    def _percorrer_pre_ordem_recursivo(self, no_atual):
        if no_atual:
            print(no_atual.valor, end=' ')
            self._percorrer_pre_ordem_recursivo(no_atual.esquerda)
            self._percorrer_pre_ordem_recursivo(no_atual.direita)

# Percurso Pós-Ordem (postorder traversal):

class ArvoreBinariaBusca:
    # (código da implementação anterior...)

    def percorrer_pos_ordem(self):
        self._percorrer_pos_ordem_recursivo(self.raiz)

    def _percorrer_pos_ordem_recursivo(self, no_atual):
        if no_atual:
            self._percorrer_pos_ordem_recursivo(no_atual.esquerda)
            self._percorrer_pos_ordem_recursivo(no_atual.direita)
            print(no_atual.valor, end=' ')
