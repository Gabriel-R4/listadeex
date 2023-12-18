# A diferença fundamental entre uma lista simplesmente encadeada (ou lista ligada simples) e uma lista duplamente encadeada está na direção dos links ou ponteiros entre os nós.

# - Lista Simplesmente Encadeada: Neste tipo de lista, cada nó tem um ponteiro que aponta para o próximo nó na sequência. Ou seja, você pode percorrer a lista apenas em uma direção, geralmente da cabeça (primeiro nó) até a cauda (último nó). Cada nó guarda uma referência para o próximo nó na sequência.

# -Lista Duplamente Encadeada: Em contraste, na lista duplamente encadeada, cada nó mantém referências para o nó anterior e para o próximo nó na sequência. Isso significa que você pode percorrer a lista tanto da cabeça para a cauda quanto da cauda para a cabeça. Isso oferece maior flexibilidade em termos de manipulação da lista, pois permite operações como a remoção de um nó sem precisar percorrer toda a lista a partir da cabeça.

# Aqui está uma comparação visual para ilustrar a diferença:

# ```
# Lista Simplesmente Encadeada:
#     Nodo 1 -> Nodo 2 -> Nodo 3 -> Nodo 4 -> None

# Lista Duplamente Encadeada:
#     None <- Nodo 1 <-> Nodo 2 <-> Nodo 3 <-> Nodo 4 -> None
# ```

# Na lista duplamente encadeada, cada nó tem duas referências (ou ponteiros), uma para o nó anterior e outra para o próximo nó na sequência, o que permite a travessia em ambas as direções. Isso oferece vantagens em algumas operações, mas também pode aumentar o consumo de memória, já que cada nó tem que armazenar duas referências em vez de uma.