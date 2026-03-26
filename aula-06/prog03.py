import os
os.system("cls")

# Dadas duas notas validas, calcular média, se não for valida, informar.

nota1 = float(input("Digite uma nota 1: "))

if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Digite uma nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"Média: {media}")
        if media >=6:
            print("Aprovado")
        else:
            print("Reprovado")   
    else:
         print(f"A nota {nota2} é invalida")    
else:
    print(f"A nota {nota1} é invalida")