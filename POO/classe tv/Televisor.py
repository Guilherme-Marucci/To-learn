class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab 
        self.modelo = modelo
        self.canal_atual = None
        self.lista_canal = []
        self.vol = 20

    def aumentaVolume(self, valor):
        if self.vol + valor <= 100:
            self.vol += valor
        else:
            self.vol = 100

    def diminuiVolume(self, valor):
        if self.vol - valor >=0:
            self.vol -= valor
        else:
            self.vol = 0

    def trocaCanal(self, canal):
        if canal in self.lista_canal:
            self.canal_atual = canal 

    def sintonizaCanal(self, canal):
        if canal not in self.lista_canal:
            self.lista_canal.append (canal)

class Controle_Remoto:
    def __init__ (self, tv):
        self.tv = tv
    def aumentaVolume(self, valor):
        self.tv.aumentaVolume(valor)

    def diminuiVolume(self, valor):
        self.tv.diminuiVolume(valor)
        
    def trocaCanal (self, canal):
        self.tv.trocaCanal(canal)
    
    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)

    
        