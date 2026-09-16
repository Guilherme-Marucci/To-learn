from Televisor import * #importa a classe televisor e o "*" representa tudo que tem dentro dela

tv = Televisor("LG", "SAMSUNG") #criando um objeto da classe Televisor, passando os parametros para inicialização dos atributos
controle =  Controle_Remoto(tv) #criando um objeto da classe Controle_Remoto, passando o objeto tv como parametro para inicialização do atributo tv

controle.sintonizaCanal("CNN")
controle.trocaCanal("CNN")

print(tv.canal_atual) #imprime o canal atual da tv, que deve ser "CNN"