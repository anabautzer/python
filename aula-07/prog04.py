import os
os.system("cls")

# Dadas 3 notas, calcular a média das duas maiores verificando se as notas são validas.

nota1 = float(input("Nota 1: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        nota3 = float(input("Nota 3: "))
        if nota3 >= 0 and nota3 <= 10:
            menor = nota1
            if nota2 < menor:
                menor = nota2
            if nota3 < menor:
                menor = nota1
            media = (nota1 + nota2 + nota3 - menor) / 2
            print(f"A média das duas maiores notas entre: {nota1:.2f}, {nota2:.2f} e {nota3:.2f} é {media:.2f}")
        else:
            print(f"Nota {nota3} inválida")
    else:
        print(f"Nota {nota2} inválida")
else:
    print(f"Nota {nota1} inválida")