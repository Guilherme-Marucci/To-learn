import random

unidade1 = input("Digite o primeiro nome ou palavra:  ")
unidade2 = input("Digite o Segundo nome ou palavra: ")
unidade3 = input("Digite o terceiro  nome ou palavra: ")
unidade4 = input("Digite o quarto nome ou palavra: ")
unidade5 = input("Digite o  quinto nome ou palavra: ")

list = [unidade1, unidade2, unidade3, unidade4, unidade5]
sort = random.choice(list)
print(f"A palavra escolhida foi : {sort}")
