import os
os.system("cls")

# exercício: a partir de uma compra, o usuário terá um desconto. Se a compra for acima de 1000 reais, terá um desconto de 10%. Se a compra for entre e (inclusive) 500 e 100, terá um desconto de 5%. Se a compra for abaixo de 500 reais, não terá desconto. Ao finalizar exiba: o valor da compra, o valor de desconto e o valor final da compra com desconto.

compra = float(input("Digite o valor da compra: R$ "))

if compra > 1000:
    desconto = compra * 0.1
   
elif compra >= 500 and compra <= 1000:
    desconto = compra * 0.05
    
else:
    desconto = 0
    
cd = compra - desconto

print(f"""
Compra......: R$ {compra:10.2f}
Desconto....: R$ {desconto:10.2f}
Valor final.: R$ {cd:10.2f}
""")
    