#LEZIONE 2
def conta(parola,lettera):
    conta=0
    for i in range(len(parola)):
        if parola[i] == lettera:
            conta=conta+1
    return conta

def numeroPrimo():
    print("Spara un numero e ti dirò se è primo")
    numero=int(input())
    print(primo(numero))

def primo(numero):
    for i in range(2,numero-1):
        if numero%i==0:
            return "Il numero non è primo"
    return "Il numero è primo"


def letteraNellaParola():
    print("Inserisci una parola")
    parola=input()
    print("Inserisci una lettera e ti dirò quante volte la lettera sta nella parola")
    lettera=input()
    print(f"La parola {parola} contiene la lettera {lettera} {conta(parola,lettera)} volte")

def minInOreEMin():
    minuti=538
    hours= minuti // 60
    mins= minuti % 60
    print(f"{hours}h {mins}min")

def quadratoEcubo():
    print("\n\n\nInserisci un numero")
    numero=int(input())
    print(f"Quadrato del numero:{numero**2}")
    print(f"Cubo del numero:{numero**3}")

def pariOdispari():
    
    print("\n\n\nControllerò se il tuo numero è pari o dispari")
    numero=int(input())
    if numero%2==0:
        print("Il tuo numero è pari!")
    else:
        print("Il tuo numero è dispari!")

def sommatoria():
    somma=0
    numero=1
    while numero!=0:
        print("Inserisci numero:")
        numero=int(input())
        somma+=numero
    print(f"Sommatoria dei numeri inseriti:{somma}")

def fattoriale():
    print("Inserisci un numero e ti calcolo il fattoriale -->  x!")
    numero=int(input())
    fattoriale=1
    for i in range(1,numero+1):
        fattoriale*=i
    print(f"{numero}! = {fattoriale}")

def contaVocali():
    print("Inserisci una frase e ti dirò quante vocali contiene")
    stringa=input()
    conta=0
    for i in range (len(stringa)):
        if(stringa[i]=="a" or stringa[i]=="e" or stringa[i]=="i" or stringa[i]=="o" or stringa[i]=="u"):
            conta+=1
    print(f"Le vocali sono:{conta}")

def tipoTriangolo():
    print("Inserisci i 3 lati di un triangolo e ti dirò che tipo di triangolo è")
    print("Lato 1:")
    lato1=int(input())
    print("Lato 2:")
    lato2=int(input())
    print("Lato 3:")
    lato3=int(input())
    if(lato1<=0 or lato2<=0 or lato3<=0):
        print("I lati di un triangolo non possono essere <= 0")
        return
    if(lato1>=lato2+lato3 or lato2>=lato1+lato3 or lato3>=lato1+lato2):
        print("I lati inseriti non formano un triangolo")
        return
    
    if(lato1==lato2 and lato2==lato3):
        print("Il triangolo è equilatero")
    elif(lato1==lato2 or lato2==lato3 or lato1==lato3):
        print("Il triangolo è isoscele")
    else:
        print("Il triangolo è scaleno")
#===========================================================
#LEZIONE 3


print("\n\nESERCIZI LEZIONE 2-3\n")
tipoTriangolo() #chiamata di funzione 
