import os
os.system("cls")

nome = "Ana Carolina" #str()
idade = 26 #int()
altura = 1.67 #float()

# formatação 1 - convercional, usando vírgula acrescenta um espaço e aceita todos os tipos/classe

print(nome, idade, altura)
print("Nome:", nome, "Idade:", idade, "Altura:", altura)
print("\nNome:", nome, "\nIdade:", idade, "\nAltura:", altura) #\n pula uma linha

# formatação 2 - usando com concatenação (junção), sinal de +

print(nome +  " " + str(idade) + " " + str(altura))
print("Nome: " + nome +  "Idade: " + str(idade) + "Altura: " + str(altura))

# formatação 3 - usando a função format()

print("{0} {1} {2}".format(nome, idade, altura))
print("Nome: {0} Idade: {1} Altura: {2}".format(nome, idade, altura))
print("Nome: {n} Idade: {i} Altura: {a}".format(n = nome,i = idade,a = altura)) #só vai funcionar nessa linha

# formatação 4 - usando f print

print(f"{nome} {idade} {altura}")
print(f"Nome: {nome} Idade: {idade} Altura: {altura}")

print(f"Nome: {nome}") #exibe e pula linha
print(f"Idade: {idade}")
print(f"Altura: {altura}")

# triplo quotes """ texto """, evita de usar print

print(f"""Nome: {nome}
Idade: {idade}
Altura: {altura}
""")