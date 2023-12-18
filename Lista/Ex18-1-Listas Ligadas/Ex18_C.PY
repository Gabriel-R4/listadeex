class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    # (Código da implementação anterior...)

    def encontrar_n_elemento_a_partir_do_final(self, n):
        ponteiro_lento = self.primeiro
        ponteiro_rapido = self.primeiro

        # Mova o ponteiro_rapido para a frente por n posições
        for _ in range(n):
            if ponteiro_rapido is None:
                return None  # Se a lista for menor que n, não é possível encontrar o n-ésimo elemento

            ponteiro_rapido = ponteiro_rapido.proximo

        # Move ambos os ponteiros até que o ponteiro_rapido alcance o final
        while ponteiro_rapido is not None:
            ponteiro_rapido = ponteiro_rapido.proximo
            ponteiro_lento = ponteiro_lento.proximo

        return ponteiro_lento.valor if ponteiro_lento else None

    # Restante do código...

# Exemplo de uso:
lista = ListaLigada()
lista.inserir(5)
lista.inserir(10)
lista.inserir(15)
lista.inserir(20)
lista.inserir(25)

lista.imprimir()  # Saída esperada: 25 -> 20 -> 15 -> 10 -> 5 -> None

n = 3
n_esimo_elemento = lista.encontrar_n_elemento_a_partir_do_final(n)
if n_esimo_elemento is not None:
    print(f"O {n}-ésimo elemento a partir do final é: {n_esimo_elemento}")
else:
    print(f"A lista não possui {n} elementos.")
