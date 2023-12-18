
# regex
# ^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$


# Essa expressão regular exige:

# - Pelo menos uma letra (maiúscula ou minúscula): `(?=.*[A-Za-z])`
# - Pelo menos um dígito: `(?=.*\d)`
# - Pelo menos um caractere especial (pode ser alterado ou expandido para incluir mais caracteres especiais): `(?=.*[@$!%*?&])`
# - Um comprimento mínimo de 8 caracteres: `{8,}`

