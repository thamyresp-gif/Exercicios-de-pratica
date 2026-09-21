
frase = "Aprender Python aqui na Alura é muito bom"

frase = frase.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ")

palavras = frase.split()

palavras_grandes = filter(lambda p: len(p) >= 5, palavras)

palavras_grandes = list(palavras_grandes)

print(palavras_grandes)


