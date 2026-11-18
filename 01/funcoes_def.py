"""
  def nome_da_funcao(**null_ou_parametros):
        # Bloco de código da função

Quando você passa paramentos dentro dos parenteses de uma fução** Você deve obrigatoriamente 
Voce atribuir um valor a cada parametro, caso contrario, o python ira retornar um erro de sintaxe.
Porém, caso você queira criar uma função que não obrigue a passagem de parametros, você pode atribuir um valor padrão a cada parametro.
"""

def mensagem1(nome):
    print( f"Hello world, {nome}!")
 
def mensagem2(nome="Usuário"):
    print( f"Hello world, {nome}!")

mensagem2()
#mensagem2("chapolin")

"""
Funções tambem podem armazenar valores com 'chave:valor', semelhante a uma dict
"""
def armazena_dados(nome, idade, sexo, filial ):
    print(f" Dados armazenados com sucesso! {nome}, {idade}, {sexo}, {filial}")

armazena_dados("Gui", 22, "M", 2)
armazena_dados(nome="Gui", idade=22, sexo="M", filial=2)
armazena_dados(**{"nome": "gui", "idade": 22, "sexo": "M", "filial": 2}) # passando um dicionario como parametro
armazena_dados() 