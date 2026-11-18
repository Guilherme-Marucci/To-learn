print("=" * 50)
print("5ª: Sistema de desconto em compras") 
print("=" * 50)

valor = float(input("Digite o valor da compra: R$ "))

if valor != 0:
    if valor > 500:
        percentual = 15
    elif valor > 200:
        percentual = 10
    else:
        percentual = 0
    
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto

    print(f"Valor original: R$ {valor:.2f}")
    print(f"Percentual de desconto: {percentual}%")
    print(f"Valor descontado: R$ {desconto:.2f}")
    print(f"Valor final da compra: R$ {valor_final:.2f}")

else:
    print("Valor inválido! Tente novamente.")