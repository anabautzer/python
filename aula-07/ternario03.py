import os
os.system("cls")

# calcular o salario liquido, descontando o inss e dando um bonus de 500 reais para todos.

salario = 10000
bonus = 500
inss = salario * 0.1 if salario > 5000 else salario * 0.05

sal_liq = salario - inss + bonus

print(salario, inss, sal_liq)