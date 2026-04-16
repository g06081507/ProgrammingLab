class Veicolo:
    def __init__(self,marca,modello,anno):
        self.marca=marca
        self.modello=modello
        self.anno=anno
        self.speed=0

    def __str__(self):
        return f"Veicolo: Marca:{self.marca} - Modello:{self.modello} - Anno:{self.anno}"
    
    def accellerare(self):
        self.speed+=5

    def frenare(self):
        if(self.speed>0):
            self.speed-=5
            
    def get_speed(self):
        return self.speed
    

    
class Auto(Veicolo):

    def __init__(self,marca,modello,anno,numero_porte):
        super().__init__(marca,modello,anno)
        self.numero_porte=numero_porte

    def __str__(self):
        return f"{super().__str__()} - Porte:{self.numero_porte}"
    
class Moto(Veicolo):

    def __init__(self,marca,modello,anno,tipo):
        super().__init__(marca,modello,anno)
        self.tipo=tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo:{self.tipo}"
    

m=Moto("Kawasaki","Ninja","1000","SI")
print(m.__str__())
m.accellerare()
m.get_speed()
m.frenare()
m.get_speed()