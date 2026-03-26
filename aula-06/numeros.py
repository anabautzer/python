import os
os.system("cls")

n = float(input("Digite um número: "))

if n > 0: # a verdade sempre vem primeiro
    print("O número é positivo!")
elif n == 0:
    print("Nulo!")
else:
    print("O número é negativo!")    
