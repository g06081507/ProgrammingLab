
class ExamException(Exception):
    pass
 
class MovingAverage:
    def __init__(self,lunghezzaFinestra):
        if not isinstance(lunghezzaFinestra,int):
            raise ExamException("Errore: La finestra non è un intero")
        if lunghezzaFinestra<=0:
            raise ExamException("Errore: La finestra non può avere un valore < = 0")
        
        self.lunghezzaFinestra=lunghezzaFinestra
    def compute(self,listaValori):
        mediaMobile=[]
        n=self.lunghezzaFinestra


        if listaValori is None:
            raise ExamException("Errore: lista valori mancante")
        if len(listaValori) == 0:
            raise ExamException("Errore: lista valori vuota")
         
        if not isinstance(listaValori,list):
            raise ExamException("Errore: non è stata inserita una lista")
        
        if n > len(listaValori):
            raise ExamException("Errore: finestra più lunga della lista")

        for i in range(len(listaValori)):
            if not isinstance(listaValori[i],(int,float)):
                raise ExamException("Errore: non tutti i valori sono int o float!")
            
    
        for i in range(len(listaValori)):
            sommaFinestra=0
            if i+n>len(listaValori):
                break
            sommaFinestra=sum(listaValori[i : i+n])
            mediaMobile.append(sommaFinestra/n)
        return mediaMobile
    
ma = MovingAverage(2)
risultato = ma.compute([1, 2, 3, 4, 5])
print(risultato)