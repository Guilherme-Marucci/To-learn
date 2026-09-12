"""
Crie um algoritmo que calcule a altura e largura de uma parede,
entrege sua área em m² e calcule quantos litros de tinta precisará e
quantas latas de tintas precisa comprar.

Cada L de tinta pinta 2m² 
cada lata tem 12L 

Se quiser, adicione uma validação para caso a parede for diferente de branca,
precisará de 50% a mais de tinta, ou seja, 1L de tinta pinta 1m²
"""
print("=" * 50,
       "\nCalculadora extremamente nixada para saber quanto de tinta precisará para sua parede \n",
       "=" * 50)
cor_parede = str(input("Sua parede é branca?\n    SOMENTE sim OU não\n"))
lata1 = 12
lata2 = 12

altura = float(input("\nQual a altura da parede\n"))
largura = float(input("\nE qual a largura?\n"))
area = altura * largura

lata1 = (area/2) / lata1
lata2 = area / lata2
L = area / 2

if cor_parede != "sim":
    print("="* 100)
    print(f"\nA area da parede é {area}M². E isso usaria em torno de {area}L de tinta")
    print(f"\nVoce precisará de {lata2:g} latas de tinta, pois sua parede terá que passar uma mão a mais! \n")
    print("="* 100, "\n")
else:
    print("=" *100)
    print(f"\nA area da parede é de {area}M². E isso usaria em torno de {L}L de tinta")
    print(f"\nVocê precisará de {lata1:.2f} latas de tinta para pintar sua parede")
    print("=" *100)
"""
elif area != int:
    print("Opa! Parece que temos uma string no meio dos valores para calculo ")
"""