print("=" * 50)
print("1ª: Cadastro de Usuário") 
print("=" * 50)

nome = input("Digite seu nome: ")

city= input("Digite sua cidade: ")

age = int(input("Digite sua idade: "))

if age >= 18 and age < 37:
    print(f"Ola, {nome}! Seja muito bem vindo, Vi que mora em {city} e tem {age} anos...")
elif age >= 37:
    print(f"Ola, {nome}! Seja muito bem vindo, Vi que mora em {city} e tem {age} anos. Ta velhinho hein! kkkk")
elif age < 18 and age > 0:
    print(f"Ola, {nome}! Seja muito bem vindo, Vi que mora em {city} e tem {age} anos. Ta cedo demais pra estar em uma facudade em! kkkk")
else:
    print("Idade inválida! Tente novamente.")
