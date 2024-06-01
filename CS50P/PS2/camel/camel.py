name = input ("camelCase: ")
word = ""
lista = []
for ch in name:
    if not ch.isupper():
        word = word + ch
    else:
        lista.append(word.lower())
        word = ch

if word not in lista:
    lista.append(word.lower())

print("_".join(lista))
