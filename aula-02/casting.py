import os
os.system("cls") # para Win, clear para Mac

# Casting - muudança de tipo da variável
conteudo = 45.7
print(conteudo, type (conteudo)) #type mostra o status (tipo/classe)
conteudo = int(conteudo) #ele vai perder o 0.7 quando for pro string por contar a partir da outra declaração
print(conteudo, type(conteudo)) #int não reconhece o 0.7
conteudo = str(conteudo)
print(conteudo, type(conteudo))
conteudo = bool(conteudo)
print(conteudo, type(conteudo)) #tudo que não é zero é verdade
