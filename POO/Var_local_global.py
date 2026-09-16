def mult_local(numero):
    a = 10 #variavel de escopo local
    print(f'Dentro da função, a var vale:{a}')
    return a * numero

a = 3 #var escopo global
b = mult_local(50)
print(f"Fora da função, vale: {a}")
print(f"A variável b vale: {b}")