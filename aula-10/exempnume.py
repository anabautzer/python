import os
os.system("cls")

numero = input("Número: ")

if numero.isnumeric():
    print(f"{numero} é um número")
else:
    print(f"{numero} não é um número")