import os
os.system("cls")

# exemplo de como segue a lógica dos operadores

tempo = 3
debito = True
aposentado = False

# resp = tempo >= 5 and not debito or aposentado

if tempo >= 5 and not debito or aposentado:
    print("Terá isenção! >:)")
else:
    print("Não terá isenção! >:(")