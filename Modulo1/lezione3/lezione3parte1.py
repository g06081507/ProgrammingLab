def sommaLista(lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma

def listaInput():
    lista = []
    elemento = input("Inserisci un elemento (INVIO per terminare): ")
    while elemento != "":
        lista.append(elemento)
        elemento = input("Inserisci un elemento (INVIO per terminare): ")
    return lista

def es1():
    numero=int(input("Inserisci numero: (0 per terminare) "))
    if not isinstance(list, int):
        raise TypeError("Devi inserire un numero intero.")
    numeri = []
    while numero != 0:
        numero=int(input("Inserisci numero: (0 per terminare) "))
        if not isinstance(numero, int):
            raise TypeError("Devi inserire un numero intero.")
        numeri.append(numero)
    print("La somma dei numeri inseriti è:", sommaLista(numeri))

def es2():
    parola = input("Inserisci una parola: ")
    if not isinstance(parola, str):
        raise TypeError("Devi inserire una stringa.")
    if (parola == parola[::-1]):
        print("La parola è palindroma.")
    else:
        print("La parola non è palindroma.")

def es3():
    lista = []
    i = input("Inserisci un numero o una stringa:")
    if i == "":
        raise TypeError("Devi inserire un numero o una stringa.")      
    while i != "":
        lista.append(i)
        i = input("Inserisci un numero o una stringa: (INVIO per terminare) ")
        
    print("Hai inserito:", lista)

    if len(lista) < 2:
        raise ValueError("Devi inserire almeno due elementi per poterli scambiare.")

    i=int(input("Inserisci l'indice i: "))
    j=int(input("Inserisci l'indice j: "))

    if i < 0 or i >= len(lista) or j < 0 or j >= len(lista):
        raise IndexError("Gli indici devono essere compresi tra 0 e " + str(len(lista)-1))
    lista[i], lista[j] = lista[j], lista[i]
    print("La lista dopo lo scambio è:", lista)

def es4():
    import random 
    print("Inserisci gli elementi della prima lista:")
    lista1 = listaInput()
    print("Inserisci gli elementi della seconda lista:")
    lista2 = listaInput()

    for numero in lista1:
        if numero in lista2:
            print("True")
            return True
    print("False")
    return False

def es5():
    lista=[]
    while True:
        i=input("Inserisci un numero: (INVIO per terminare) ")
        if i=="":
            break
        if not i.isdigit():
            raise TypeError("Devi inserire un numero.")
        i=int(i)
        if i<0 or i>9:
            raise ValueError("Devi inserire un numero compreso tra 0 e 9.")
        lista.append(i)


    listaParole=["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
    listaNumeriParole=[]
    for numero in lista:
        listaNumeriParole.append(listaParole[numero])
        print(listaParole[numero])
    
es5()