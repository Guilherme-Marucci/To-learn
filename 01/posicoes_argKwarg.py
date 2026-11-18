
    ################################################################
                #    arg e kwargs
    ################################################################
"""
Podemos combinar parâetros obrigatorios com args e kwargs. Quando são definos (*args & **kwargs), 
 o método recebe os valores como _TUPLA_ E _DICIONARIO_ respectivamente
 OBS: Só é obritorio o uso de *qqrcoisa e ** qqrcoisa. 
 Não é obrigatorio serem definidos com seus respectivos nomes. 
"""


    # Args são tuplas e kwargs são dicionarios 
def poema(data, *args, **kwargs):
    texto = "".join(args) # .join esta cocatenando todos valores de args com "\n"
    meta_dados = "".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    #^^^ Desenha um texto no formato Chave:Valor e armazenando na memoria  
    mensagem = f"{data} \n\n{texto}\n\n{meta_dados}"
    print(mensagem)
print("~" * 50)

poema("Tudo que eu quero, sossego! *", "Do leme ao pontal*", autor="Tim maia**", ano=1991**1)

""""
kwarg ja é um dicionario invisivel, que guarda pares reais de chave e valor. Oque a linha
10 faz é transforma esses dados brutos em Algo mais organizado(join([f"{chave.title()}: {valor})

"""
# Kwargs.items() 
""" 
Abstraindo  **kwargs como uma caixa com etiquetas adesivas.
essa expressão pega cada etiqueta colada e entraga a dupla pronta:
 ("autor", "Tim maia") e depois ("ano", 1991).
"""
# for chave, valor in
"""
Como um robo pegador. Pega uma dupla por vez. Na primeira coleta *Chave* é "autor" e valor é "Tim maia"
"""
#f"{chave.title()}: {valor}"
"""
Aqui é o texto visualmente organizado. "chave.title()" pega a palavra autor e troca primeira letra para maiuscula(TITLE)
':' neste contexto é apenas um char. Pois no py f-strg só executa funções dentro das chaves {} 
ele só possui comportamento funcional em um dicts reais  dict = {" ": " "}
e f-strg para formatação f"{num:.2f}"
"""

# {valor} = "Tim maia"

# paramêtro especiais 
""" Podem ser passados tanto por poisção quanto pelo seu nome exato, 
 para melhor legibilidade se os itens são passados por nome, nome e posição ou somente posição.
"""
def carro(modelo, ano, /, cor, *, placa, motor):
   print(modelo, ano, placa, cor, motor)

def f(pos1, pos2, /, pos_kwd, *, kwd1, kwd2):
 #    ^---------^   ^-------^    ^--------^
 #   só posicional  posi+nome     só nome 
    f.pos1 = carro.modelo
    f.pos2 = carro.ano
    f.pos_kwd = carro.cor
    f.kwd1 = carro.placa 
    f.kwd2 = carro.motor



carro("Mitshubish Eclipse", 1998, "Vermelho", placa = "ABC1D23", motor = "V4- BI TURBO")
print (carro) # atua como ponteiro do objeto na memoria 

def firstClass(explica):
    return True;

firstClass.explica = ("""Em python, TUDO é objeto, funções também são entendidas como objeto
sendo categorizadas como objetos de primeira classe. com isso, podemos atribuir funções 
a variaveis, passar como paramentro para outra função, usar como valores em estrutura de dados
e como Closures(Valor de retorna p/ função)""")