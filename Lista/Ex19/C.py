
# ^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$

# Essa expressão regular corresponde a datas seguindo as seguintes regras:

# - `(0[1-9]|[12][0-9]|3[01])`: Para o dia (DD), aceita valores de 01 a 31. A expressão verifica se o dia começa com 0 e depois um número de 1 a 9 (01 a 09), ou se começa com 1 ou 2 seguido por qualquer número (10 a 29) ou se começa com 3 seguido por 0 ou 1 (30 ou 31).
# - `/(0[1-9]|1[0-2])`: Para o mês (MM), aceita valores de 01 a 12. A expressão verifica se o mês começa com 0 e depois um número de 1 a 9 (01 a 09) ou se começa com 1 seguido por 0 a 2 (10 a 12).
# - `/\d{4}`: Para o ano (AAAA), espera-se um número de quatro dígitos.
