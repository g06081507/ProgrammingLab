from datetime import datetime, date, timedelta


def es5():

    print("\n\n")
    while True:
        try:
            giorno = int(input("Inserisci un giorno: "))
            mese = int(input("Inserisci un mese: "))
            anno = int(input("Inserisci un anno: "))
            compleanno = date(anno, mese, giorno)
            break
        except ValueError:
            print("Errore: inserisci una data valida (numeri interi).")
    
    bisestile = False
    if anno % 4 == 0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                bisestile = True
        else:
            bisestile = True
  
    questAnno = date.today().year

    prossimoCompleanno = date(questAnno, compleanno.month, compleanno.day)
    if prossimoCompleanno < date.today():
        prossimoCompleanno = date(questAnno + 1, compleanno.month, compleanno.day)
    print(f"Il tuo prossimo compleanno sarà il: {prossimoCompleanno}")

    countdown=datetime(prossimoCompleanno.year, prossimoCompleanno.month, prossimoCompleanno.day) - datetime.now()
    print(f"Il tuo prossimo compleanno è tra {countdown.days} giorni e {countdown.seconds//3600} ore,")
    print(f"{countdown.seconds%3600//60} minuti e {countdown.seconds%60} secondi")


def es6():
    while True:
        try:
            n=int(input("Inserisci un numero intero: "))
            break
        except ValueError:
            print("Errore: inserisci una data valida (numeri interi).")
    print("Il quadrato del numero è:", n**2)

def inserisciNumero():
    while True:
        try:
            print("\n")
            numero=float(input("Inserisci un numero: "))
            break
        except ValueError:
            print("ERRORE: Deve esser inseito un numero riconducibile a intero")
    return numero

def es7():
#non sapevo se usare il match perché non esiste lo switch
    while True:
        print("MENU:")
        print("1) Somma tra 2 numeri")
        print("2) Differenza tra 2 numeri")
        print("3) Uscita dal programma")
        print("\n")
        try:
            n=0
            n=int(input("Scegli un'opzione valida (1 2 3):"))
            if n<1 or n>3:
              raise ValueError   
        except ValueError:
            print("\nIl valore non è accettato tra le opzioni:\nInserisci una di queste opzioni 1 2 3")
        if n==1:
                n1=inserisciNumero()
                n2=inserisciNumero()
                print(f"\nLa somma tra i due numeri è: {int(n1+n2)}")
        if n==2:
                n1=inserisciNumero()
                n2=inserisciNumero()
                print(f"La differenza tra i due numeri è: {int(n1-n2)}")
        if n==3:
                print("Uscita dal programma...")
                break
            
es7()   
