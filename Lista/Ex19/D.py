# ```
# \b(?:https?|ftp):\/\/\S+\b
# ```

# Essa expressão regular busca por padrões que correspondem a URLs seguindo algumas regras:

# - `\b`: Indica uma fronteira de palavra, garantindo que a correspondência comece no início de uma palavra.
# - `(?:https?|ftp)`: Procura por "http", "https" ou "ftp".
# - `:\/\/`: Procura pelo padrão "://".
# - `\S+`: Corresponde a um ou mais caracteres que não sejam espaços em branco, representando o domínio da URL.
# - `\b`: Indica outra fronteira de palavra, garantindo que a correspondência termine no final de uma palavra.
