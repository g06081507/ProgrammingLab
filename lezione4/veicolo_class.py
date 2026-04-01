class Veicolo:
    def __init__(self,marca,modello,anno,speed):
        self.marca=marca
        self.modello=modello
        self.anno=anno
        self.speed=speed

    def __str__(self):
        return f"Veicolo: Marca:{self.marca} - Modello:{self.modello} - Anno:{self.anno}"
    
    def accellerare(self):
        self.speed+=5

    def frenare(self):
        if(self.speed>0):
            self.speed-=5
            
    def get_speed(self):
        return self.speed
    

    
        