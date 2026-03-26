import os
os.system("cls")

# Dada uma nota, informar se ela é válida ou não (entre 0 e 10)

nota = float(input("Digite uma nota: "))

if nota >= 0 and nota <= 10:
    print("A nota é valida")
else:
    print("A nota é invalida")