import os
os.system("cls")

# pré-condicional while

# forçar o usuário digitar um número, com zero erros ou vários

# calcular o dobro de um número dado pelo usuário
numero = input("Número: ")

# while so aceita true
# tratamento da não digitação de um número
while not numero.isnumeric(): # enquanto não for um número, faça
    print("Erro! Não digitou um número")
    numero = input("Número: ")
else: #utilizado quando não tem interrupção
    numero = float(numero) # mudança de String para float

print("Dobro: ", numero + numero)

