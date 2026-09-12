print("=" * 50)
nome = input("Nome: ")
saldo = 10000 # pai ta rich
print(f"Olá, {nome}!")
print(f"Seu saldo é: R$ {saldo:.2f}")
saque = float(input("Digite o valor do saque: "))

if saque > saldo:
    print("Saldo insuficiente!")
elif saque <= 0:
    print("Valor de saque inválido!")
else:
    saldo -= saque
    print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
print("=" * 50)