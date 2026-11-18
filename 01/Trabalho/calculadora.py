print("=" * 50)
print("2ª: Calculadora") 
print("=" * 50)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")

if num2 == 0:
    print("Divisão: Não é possível dividir por zero. \n Passei no teste?")
else:
    print(f"Divisão: {num1 / num2}")