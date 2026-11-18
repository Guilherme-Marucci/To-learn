print("=" * 50)
print("3ª: Verifidor de número par ou impar") 
print("=" * 50)

numero = int(input("Digite um número inteiro: "))

if numero <= 0:
    print("Número inválido! Digite um número maior que zero.")
elif numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")