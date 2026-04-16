class Canguro:
    def __init__(self,contenuto_tasca=[]):
        self.contenuto_tasca=[]
    def intasca(self,x):
        self.contenuto_tasca.append(x)
    def __str__(self):
        return self.contenuto_tasca

c=Canguro()  
x=0
while x!="ESCI":
    print("Inserisci un oggetto in tasca, quello che vuoi!\nScrivi 'ESCI' per terminare")
    x=input()
    if(x!="ESCI"):
        c.intasca(x)

print(c.__str__())