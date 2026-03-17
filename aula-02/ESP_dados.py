import os
os.system("cls") # para Win, clear para Mac

# input - comando de entrada de dados | input sempre lê str()
# print - comando de saída de dados

valor = input("Digite algo: ")
print(type(valor))
valor = int(valor)
print(type(valor))
resp = valor + valor
print(resp)

# outra forma de fazer
valor = int(input("Digite algo: "))
resp = valor + valor
print(resp)