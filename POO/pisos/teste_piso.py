import math
from area_piso import Area

while True: #inicia um loop infinito para permitir que o usuário faça várias consultas sem precisar reiniciar o programa
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite outro lado para o piso: "))

    piso = Area(piso_a, piso_b)
    az_a = float(input("digite o primeiro lado do azulejo: "))
    az_b = float(input("digite o segundo lado do azulejo: "))

    azulejo = Area(az_a, az_b)#criando um objeto da classe Area para representar o azulejo, passando os lados do azulejo como parametros para a inicialização dos atributos da classe

    area_piso =  piso.area()#calcula a area do piso usando o metodo area da classe Area, passando os lados do piso como parametros para o metodo
    area_az = azulejo.area()#calcula a area do azulejo usando o metodo area da classe Area, passando os lados do azulejo como parametros para o metodo

    quant_az = area_piso / area_az

    if area_piso % area_az == 0:
        print(f"A quantidade de azulejos necessária para cobrir o piso é: {quant_az}")
    else: 
        print(f"A quantidade mínima de azulejos necessária para cobrir o piso é: {math.ceil(quant_az)}") # 'math.ceil arredonda o numero para mais, caso valor haja casas decimais

    if area_piso % area_az != 0:
        break #interrompe o loop infinito após a primeira consulta, para evitar que o programa continue solicitando entradas do usuário indefinidamente
