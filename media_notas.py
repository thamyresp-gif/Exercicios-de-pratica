
#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

n_nota1 = float(input("Digite o valor da nota 1: ").replace(",","."))
n_nota2 = float(input("Digite o valor da nota 2: ").replace(",","."))
n_nota3 = float(input("Digite o valor da nota 3: ").replace(",","."))

media = (n_nota1 + n_nota2 + n_nota3) / 3

print (f"O valor da media das notas é {media}")
