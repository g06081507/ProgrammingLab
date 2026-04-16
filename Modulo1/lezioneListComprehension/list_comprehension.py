def es1():#numeri pari tra 0 e 9
    list=[i for i in range (9) if(i%2!=0)]
    print(list)
def es2():#concateno
    input=[[1,2,3],[4,5],[6,7,8,1]]
    list=[i for nListeRosa in input for i in nListeRosa ]
    print(list)
def es3():#metto nella lista se il prodotto (controllando tutte le possibili combinazioni, fa + do 10)
    list_a=[1,3,5,7]
    list_b=[2,4,6]
    l=[nA*nB for nA in list_a for nB in list_b if(nA*nB)>10]
    print(l)
def es4():#controllo terne pitagoriche da 1 a 20
    listSENZARIPETIZIONI=[[a,b,c] for a in range(1,21) for b in range(a,21) for c in range(b,21)  if((a**2)+(b**2)==(c**2))]
    listCONRIPETIZIONI=[[a,b,c] for a in range(1,21) for b in range(1,21) for c in range(1,21)  if((a**2)+(b**2)==(c**2))]
    print(f"SENZA RIP:{listSENZARIPETIZIONI}" + "\n")
    print(f"CON RIP:{listCONRIPETIZIONI}")
def es5():
    list_a=[0,1,3,4]
    list_b=['a','b','c']
    list=[[a,b] for a in list_a for i,b in enumerate(list_b) if(a%2==0 and i%2!=0)]
    print(list)
def es6():
    frase="the cat sat on the mat the cat"
    listParola=frase.split(" ")
    #out=[[parola, listParola.count(parola)] for parola in listParola]
    dizio  = {parola : listParola.count(parola) for parola in listParola}
    print(dizio)
    
es6()
