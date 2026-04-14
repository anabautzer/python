import os
os.system("cls")

salario = float(input("Salário: "))
vendas = float(input("Vendas: "))
bonus = 1000

ganho = (vendas * 0.06 if vendas > 10000 else vendas * 0.04) + bonus

print(f"Ganho final é: R${ganho}")