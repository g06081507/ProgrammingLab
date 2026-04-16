class CSVFile:
    def __init__(self, nome):
        self.nome = nome

    def get_data(self, nomeFile):
        try:
            with open(nomeFile, "r") as file:
                lista = []
                for riga in file:
                    lista.append(riga.split())
                return lista
        except (FileExistsError, FileNotFoundError):
            print("Il file non è stato trovato o c'è stato un errore\n\n")

    def printLista(self, lista):
        if lista is None:
            print("Nessun dato da stampare")
            return
        for i in lista:
            print(i)


class NumericalCSVFile(CSVFile):
    def get_data(self, nomeFile,start,end):
        try:
            with open(nomeFile, "r") as file:
                lista = []
                for i, riga in enumerate(file):
                    if i == 0 or i<start or i>end:
                        continue  # salta riga
                    riga = riga.strip()              # rimuove \n
                    campi = riga.split(",")          # split su virgola
                    if len(campi) < 2:
                        continue  # riga malformata
                    data = campi[0]
                    valore = float(campi[1])
                    lista.append((data, valore))
                return lista
        except (FileExistsError, FileNotFoundError):
            print("Il file non è stato trovato o c'è stato un errore\n\n")

start=0
end=0
while start>=end:
    print("Da che riga vuoi leggere?")
    start=int(input())
    print("Fino a?")
    end=int(input())
file = NumericalCSVFile("shampoo.csv")
file.printLista(file.get_data(file.nome,start,end))