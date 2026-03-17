import os
os.system("cls") # para Win, clear para Mac

# Operadores aritméticos

n1 = 10
n2 = 3
resp = n1 + n2
print(resp, type(resp)) 
resp = n1 - n2
print(resp, type(resp)) 
resp = n1 * n2
print(resp, type(resp)) 
resp = n1 / n2
print(resp, type(resp)) #ele muda o tipo para se adequar a resposta
resp = n1 // n2 #divisão inteira, só o resultado sem a virgula
print(resp, type(resp)) 
resp = n1 % n2 #módulo mostra o resto da divisão
print(resp, type(resp))

n1 = 17
n2 = 7
resp = n1 // n2
print(resp, type(resp)) 
resp = n1 % n2
print(resp, type(resp)) 

n1 = 12.5
n2 = 5.1
resp = n1 // n2
print(resp, type(resp)) 
resp = n1 % n2
print(resp, type(resp)) #py aceita número fracionado para fazer módulo 

n1 = 15
n2 = 4
resp = n1 + n1 * n2 / 2 - n2 #ele entende as prioridades para fazer o cálculo
print(resp, type (resp))
resp = n1 % n1 // n2 / n1 * n2
print(resp, type (resp))

resp = 2 ** 3 #exponenciação
print(resp)

# Operadores literais (texto)

resp = "34" + "34"
print(resp)
n1 = 34
resp = n1 * 4 #variavel string só pode multiplicar por número, não com outra váriavel
print(resp)