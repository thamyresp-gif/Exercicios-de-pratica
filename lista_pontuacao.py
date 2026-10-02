
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',

                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',

                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']


lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',

                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',

                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']



def palavras_pontuacao(lista):
    for palavra in lista:
        if "," in palavra or "." in palavra or "!" in palavra or "?" in palavra:
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')

palavras_pontuacao(lista_tratada)

try:
    palavras_pontuacao(lista_nao_tratada)
except ValueError as e:
    print(f"{type(e).__name__}: {e}")