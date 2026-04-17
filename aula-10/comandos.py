import os
os.system("cls")

# calcular o dobro de um número dado pelo usuário

# faça o laço repita (while True)
while True:
    numero = input("Número: ")
    if not numero.isnumeric():
        print("Erro! Não digitou um número")
        continue
    else:
        break

numero = float(numero) # conversão fora do laço
print("Dobro: ", numero + numero)