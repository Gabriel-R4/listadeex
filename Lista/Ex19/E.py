import re

texto = "Aprender é importante para crescer. Aprender constantemente é fundamental."

palavra_antiga = "Aprender"
palavra_nova = "Desenvolver"

novo_texto = re.sub(r'\b' + palavra_antiga + r'\b', palavra_nova, texto)
print(novo_texto)


