#aula sexta feira 04/09


print("                ======= SISTEMA DE ESTACIONAMENTO =======")
print("Responda apenas com 'moto' ou 'carro' para evitar erros e porque estou com preguiça \n de estender demais o algoritmo. \n")
print("="* 70, "\n")
print("=== permanência menor que uma hora é gratuito e não precisa de cadastro!! === \n")
print("Acima de 10 horas valor fixo de 90 reais para carros e 60 reais para motos. \n")

veiculo = input("Seu veículo é uma moto ou um carro? ").lower() 
placa = input("Digite a placa do veículo: ")
modelo = input("Escreva a marca e modelo do carro: ")
horas = int(input("Digite o tempo de permanência (em horas): "))
valor = 0.0

if veiculo == "carro": 
    if horas <= 0:
        print("Você não precisa efetuar pagamento, siga sua vida normalmente. ")
    elif horas <= 1 and horas <= 10:
        valor = 8.00 * horas
    else:
        valor = 90.00
else: 
    if horas <=0:
        print("Você não precisa efetuar pagamento, siga sua vida normalmente. ")
    elif horas >=1 and horas <=10:
        valor = 5  * horas
    
    else: 
        valor = 60.00
 
print(f"\n{veiculo}, {modelo} de placa {placa}: Total a pagar = R$ {valor:.2f}")
 