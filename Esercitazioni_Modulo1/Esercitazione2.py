class ExamException:
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
    
    def checkParti(self,parti):
        try:
            valore=int(parti[1])
        except: 
            return False
        if not "-" in parti[0]:
            return False
        annoEmese=parti[0].split("-")
        try:
            annoEmese[0]=int(annoEmese[0])
            annoEmese[1]=int(annoEmese[1])        
        except:
            return False
        if annoEmese[1] < 1 or annoEmese[1] > 12:
            return False
        return True


    
    def get_data(self):
        try:
            file = open(self.name, "r")
        except:
            raise ExamException("ERRORE: file non trovato!")        
        listaAnni=[]
        dataPrecedente=None
        for riga in file:
            riga=riga.strip()
            if riga.startswith("date"):
                continue
            if not riga or not "," in riga:
                continue
            else:
                parti=riga.split(",")
                if len(parti)<2 or not self.checkParti(parti):
                    continue
                else: #se self.checkParti(parti)e len è >=2 allora ok

                    valore=int(parti[1]) #posso farlo perché non da errore nel checkparti
                    if dataPrecedente is None:
                        dataPrecedente=parti[0]
                        listaAnni.append([parti[0],valore])

                    else:
                        if dataPrecedente>=parti[0]:
                            raise ExamException("Data non in ordine o duplicata!")
                        else:
                            dataPrecedente=parti[0]
                            listaAnni.append([parti[0],valore])
        file.close()
        return listaAnni


def compute_variations(time_series, first_year, last_year):
    dizio={}
    for data,valore in time_series:
        anno=int(data.split("-")[0])
        if first_year <= anno and anno <= last_year:
            if not anno in dizio:
                dizio[anno]=[]
            dizio[anno].append(valore)


    anni=list(dizio)
    dizioVariazioni={}
    print("2)")
    for i in range(len(dizio) - 1):
        mediaStoAnno=sum(dizio[anni[i]])/len(dizio[anni[i]])
        mediaProssimoAnno=sum(dizio[anni[i+1]])/len(dizio[anni[i+1]])
        try:
            stringa=str(anni[i])+"-"+str(anni[i+1])
        except:
            raise ExamException("Errore nella conversione degli anni")
        dizioVariazioni[stringa]=[]
        dizioVariazioni[stringa].append(mediaProssimoAnno-mediaStoAnno)

        #L'esercizio 2 è comdo da fare qui
        print(anni[i],":",mediaStoAnno)


    print("3)")
    return dizioVariazioni



time_series = CSVTimeSeriesFile("data.csv").get_data()
print("1)")
for elemento in time_series:
    print(elemento)


first_year=1949
last_year=1956
if first_year>last_year:
    raise ExamException("Anni inseriti non validi: Gli anni devono essere in ordine")

for intervallo,variazioni in compute_variations(time_series, first_year, last_year).items():
    print(intervallo,":",variazioni)
       
        


#DA QUI INUTILE ( MA LO LASCIO PERCHE' NON COSTA NULLA)
def raggruppoPerAnno (lista):
    dizio = {}
    for item in lista:
        items = item.split(",")
        annoMese = items[0].split("-")
        value = items[1]
        anno = annoMese[0]
        #mese = annoMese[1]
        if not anno in dizio:
            dizio[anno]=[]
        dizio[anno].append(value)
    return dizio

def mediaPerAnno(dizio):
    mediaPerAnno=[]
    for anno in dizio:
        media=mediaElementsLista(dizio[anno])
        mediaPerAnno.append(media)          
    return mediaPerAnno
            
def variazioneMediaTraAnni(dizio):
    listaMedie=mediaPerAnno(dizio)
    listaVariazione=[]
    anni=list(dizio)
    for i in range(len(anni)-1):
        stringa=anni[i+1], "-",anni[i]," : ",float(listaMedie[i+1]-listaMedie[i])
        listaVariazione.append(stringa)
    return listaVariazione

def mediaElementsLista(lista):
    listNumerica= [float(x) for x in lista]
    return sum(listNumerica)/len(listNumerica)

def stampaSottoliste(listaMedie,dizio):
    for anno,media in zip(list(dizio),listaMedie):
        print(anno,": ",media)
def stampaDizio(dizio):
    for anno,valore in dizio.items():
        print(anno,": ",valore)


