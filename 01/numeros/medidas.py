#   Conversor de medidas aritméticas
#    Crie um algoritmo que leia a distancia em metros e converta
#   para centímetros, milímetros, quilômetros e milhas.
#   a o finalizar, faça uma iteração adicionando a opção de escolher qual
#   conversão será feita.



print("===========================================\n" \
"\n     Conversor de medidas aritméticas\n" \
"\n===========================================\n");


num = int(input("Digite a distância em metros: "))

km = num / 1000
hm = num / 100
dam = num / 10 
dm = num * 10
cm = num * 100
mm = num * 1000

print("===================================================\n" \
f"\n     {num}m Em diferentes unidades de medida\n" \
"\n===================================================\n");



"""
print(f"{km}Quilômetros\n~~~~~~~~~~~~~~~~~~~~~~")
print(f"{hm}Hectômetros \n~~~~~~~~~~~~~~~~~~~~~")
print(f"{dam}Deacâmetros\n~~~~~~~~~~~~~~~~~~~~~")
print(f"{dm}Decímetros\n~~~~~~~~~~~~~~~~~~~~~")
print(f"{cm}Centímetros\n~~~~~~~~~~ ~~~~~~~~~~~")
print(f"{mm}Milímetros\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
"""