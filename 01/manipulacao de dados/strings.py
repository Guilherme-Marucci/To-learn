import os
print("=" *50)
print("Manipulação de textos em python")
print("=" *50)

frase1 = "Eu odeio a Julia"

print(f"Frase orignal:\n {frase1}")

print(f"Comprimento da frase: {len(frase1)}")
#retorna ou altera o comprimento da string 
print("Função count: ",frase1.count("u", 0, 15))
print("Função find: ",frase1.find("ia"))
print("Função find qunado não há: ",frase1.find("Ainda amo?"))
print('amo' in frase1) #Bool para conferir se ha o dado dentro da varialvel
print("Função replace: ",frase1.replace('Ainda', 'amo'))
print("upper: ",frase1.upper())#Joga tudo pra maiusculo 
print("lower: ",frase1.lower())#Joga tudo para minusculo
print("Captalize: ",frase1.capitalize())# formata deixando somente a primeira letra  de toda string em maícusla
print("title: ",frase1.title())# analiza quantas palavras tem na strg, identifica os espaços em braco e torna a primeira letra de cada palavra maiuscula

frase2 = "   Quero a agua do mar   "
print("strip: ",frase2.strip())# Remove espaços em branco no inicio e no final
print("r: ",frase2.rstrip())# r = right. ou seja, irá remover somente da direita
print("l: ",frase2.lstrip())# mesma logica

print("split: ",frase1.split())#remove os espaços em branco e transforma cada palavra em uma lista. neste caso, uma lista do 0 ao 3
"_".join(frase1)# junta uma lista de strings com Qualquer caractere dentro do "" entre cada item
print(f"""
         As variaveis não são alteradas enquanto não usar 
        a expressção var = var.função(). veja: 
            {frase1} 
            {frase2}""") # Ao usar 3 aspas tu pode identar como quiser o texto



