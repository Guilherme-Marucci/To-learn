produto = str(input("Digite o nome do produto: "));
quantidade = int(input("Quantidade: "))
price = float(input("Preço: "))

total = (price *quantidade)

if quantidade >=5:
    total - (100 * 0.5)
print(f" Produto: {produto}\n")
print(f" Quatidade: {quantidade}. \n Preço: ${price}\n Total: ${total}")
