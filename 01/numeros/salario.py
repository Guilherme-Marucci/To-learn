print("=" * 100)
print("\n                 Aprenda a ser indiferente ao que não faz diferênça \n")
print("=" * 100, "\n")

salario = float(input("Me diga seu salario e eu direi quanto deve receber a mais... \n"))
novo = 0
if salario > 7000 and salario <= 9000:
    novo = salario - (salario *(3/100))
    print("Você já ganha bem, merece um reajuste de acordo com a inflação atual...")
    print(f"\n seu salario passará a ser:  {novo}$")
elif salario >= 5000 and salario <= 7000:
     novo = salario - (salario *(7/100))
     print("Você já sofre um pouco mais. Merece um reajuste maior")
     print(f"Seu novo salario será:  {novo}$")

elif salario > 2600 and salario < 5000:
    novo = salario - (salario *(10 / 100))
    print(f"Aqui já falamos de dificuldades para se manter no brasil... {novo}")
else:
    work = str(input("Você trabalha? "))
    if work != "sim" or work != "sim":
        print("Então esse sistema não serve pra você, não me faça perder tempo!")
    else: 
        print("Filho(a), você precisa de uma cesta? Alguma ajuda financeira? Um emprego diferente, talvez...")

       
