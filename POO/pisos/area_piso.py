class Area:
    def __init__ (self, lado_a, lado_b): #define o objeto inicial e seus atributos
        self.a = lado_a
        self.b = lado_b
     
    def muda_valor(self, novo_a, novo_b): 
       self.a = novo_a
       self.b = novo_b

    def retorna_lado(self):
        print (f'O retângulo tem os lados {self.a} e {self.b}')

    def area(self):
        return self.a * self.b
    