

gabarito = ['D', 'A', 'B', 'C', 'A']

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def calcular_notas(gabarito, testes):
   
    for teste in testes:
        for alternativa in teste:
            if alternativa not in ['A', 'B', 'C', 'D']:
                raise ValueError(f"A alternativa {alternativa} não é uma opção de alternativa válida")


    notas = []
    for teste in testes:
        nota = 0
        for i in range(len(gabarito)):
            if teste[i] == gabarito[i]:
                nota += 1
        notas.append(nota)

    
    return notas