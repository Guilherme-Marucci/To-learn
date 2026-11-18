"""
Dicionarios são conjuntos de dados armazenados em pares
Chave:valor, onde a chave é única e o valor pode ser qualquer tipo de dado.
alem disso, são variaveis mutaveis. 

"""

dados = {"email@email.com.br": {"nome": "guilherme", "idade": 20, "sexo": "masculino"}}
dados.update({"Email2@email.com": {"nome": "Gui", "Idade": 25}}) # atualiza o dicionario com os valores passados, caso a chave não exista, ele cria 
print(dados.get["nome"]) # Retorna o valor do dicionario na posição 1, caso não exista, retorna None
print (dados)
dados.get("nome") # retorna o valor da chave nome, caso não exista, retorna None
dados.get("faca", {}) # caso não encontra ele ira retornar o dicionario vazio 
                       #ou oque for passado no segundo parametro ({})
dados.setdefault("numero", 10) # caso a chave não exista, ele cria a chave com o valor passado no segundo parametro
result = dados.pop("email@email.com.br", {}) # remove o item do dicionario e retorna o valor da chave, caso não exista, retorna o dicionario vazio
print(result, "Removeu um item do dicionario")
print(dados, "retornou somente um item por conta do dados.get  ('faca', { }) ")
print(dados, "Arualizou todo o dicionario com os valores")
print(dados.values(), "Retorna somente os dicionarios amarrados com a chave")
print("=" * (4 ** 3))

dados = {
    "email@email.com.br": {"nome": "guilherme", "idade": 20, "sexo": "masculino"},
    "ana@email.com.br": {"nome": "ana", "idade": 40, "sexo": "feminino"},
    "email2@email.com.br": {"nome": "bruna", "idade": 18, "sexo": "feminino"},
    "email3@email.com.br": {"nome": "camilla", "idade": 29, "sexo": "feminino"},
}
result = "email@email.com.br" in dados #Bool: Retoranara True
print(result)