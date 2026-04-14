import os
os.system("cls")

# Dada uma nota verificar se ela é valida ou não.

nota = float(input("Nota: "))

if nota >= 0 and nota <= 10:
    print("Nota válida")
else:
    print("Nota inválida")

# Dadas 3 anos, calcular a média das duas maiores verificando se as notas são validas.