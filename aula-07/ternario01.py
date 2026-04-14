import os
os.system("cls")

# ternário: condição composta onde só aceita uma instrução no lado verdade e outra no falso. Ele substitui o if + else.

# regra (sintaxe): variavel = instrução true if condição else instrução false

idade = int(input("Idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("Maior de idade") if idade >= 18 else print("Menor de idade")