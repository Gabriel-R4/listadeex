def verifica_balanceamento(sequencia):
    pilha = []
    mapeamento = {')': '(', '}': '{', ']': '['}

    for caractere in sequencia:
        if caractere in '({[':
            pilha.append(caractere)
        elif caractere in ')}]':
            if not pilha or pilha[-1] != mapeamento[caractere]:
                return False
            pilha.pop()

    return len(pilha) == 0

# Exemplo de uso:
sequencia_1 = "{[()]}"
sequencia_2 = "{[(])}"
sequencia_3 = "()()()"

print(verifica_balanceamento(sequencia_1))  # Saída esperada: True
print(verifica_balanceamento(sequencia_2))  # Saída esperada: False
print(verifica_balanceamento(sequencia_3))  # Saída esperada: True
