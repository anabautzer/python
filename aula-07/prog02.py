import os
os.system("cls")

# Dadas 3 notas, verificar e exibir qual é a de menor valor.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

menor = nota1
if nota2 < menor:
    menor = nota2

if nota3 < menor:
    menor = nota1

print(menor)