def sommaValoriShampoo(filename):
    with open(filename, "r") as f:
        somma = 0
        for line in f:
            split_line = line.split(",")
            if split_line[0].lower() == "data":
                continue
            if len(split_line) < 2:
                continue
            try:                
                valore = float(split_line[1])
            except ValueError:  
                continue
            somma += float(split_line[1])
    print(somma)
    return somma


def conta_presenzeLista(lista):
    dizio={}
    for elemento in lista:
        if elemento in dizio:
            dizio[elemento] += 1
        else:
            dizio[elemento] = 1
    print(dizio)
    return dizio

def conta_presenzeFile(filename):
    dizio={}
    with open(filename, "r") as f:
        for line in f:
            parole = line.split()
            for parola in parole:
                if parola in dizio:
                    dizio[parola] += 1
                else:
                    dizio[parola] = 1
    print(dizio)
    return dizio

def noDuplicate(filename):
    lista=[]
    with open(filename, "r") as f:
        for line in f:
            if not line.strip() in lista:
                lista.append(line.strip())
        with open("unique.txt", "w") as f:
            for parola in lista:
                f.write(parola + "\n")
    print(lista)
    return 
    
#conta_presenzeLista(["ciao", "mondo", "ciao", "python"])
#sommaValoriShampoo("shampoo.csv")
#conta_presenzeFile("ciao.txt")
noDuplicate("ciao.txt")