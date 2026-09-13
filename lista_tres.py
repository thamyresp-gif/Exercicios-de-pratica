

numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]



def multiplos_de_3(numeros):
    lista = []
    for i in (numeros):
         if i % 3 == 0:
            lista.append(i)

    return(lista)

mult_3 = multiplos_de_3(numeros)
print(mult_3)

