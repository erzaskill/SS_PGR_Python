def soucin():
    a=float(input("Zadej číslo: "))
    b=float(input("Zadej druhé číslo: "))
    print(a*b)
#soucin()






def kladnezaporne():
    a=float(input("Zadej číslo: "))
    if a<0:
        print("Číslo je zaporné!! ")
    elif a==0:
        print("Číslo se rovná 0 ")
    else:
        print("Číslo je kladné!! ")

#kladnezaporne()

def maxprum():
    a=float(input("Zadej číslo: "))
    b=float(input("Zadej číslo: "))
    if a>b:
        max = a
    else:
        max = b
    print ("Max: " + str(max) + "\n prumer: " + str((a+b)/2))

#maxprum()

def cyklusWhile():
    a=1
    soucet= 0
    pocet= 0
    while (a!=0): #a!=0 znamená různé od nuly
        a=float(input("Zadej číslo: "))
        soucet= soucet + a
        pocet= pocet + 1
    print(soucet/(pocet-1))

#cyklusWhile()


def cyklusWhile2():
    a=1
    soucet= 0
    pocet= 0
    while (a>0): #a!=0 znamená různé od nuly
        a=float(input("Zadej číslo: "))
        if (a>0):
            soucet= soucet + a
            pocet= pocet + 1
    print(soucet/(pocet))

#cyklusWhile2()

def cyklusWhile3():
    a=1
    soucet= 0
    pocet= 0
    a=float(input("Zadej číslo: "))
    while (a>0): #a!=0 znamená různé od nuly         
            soucet= soucet + a
            pocet= pocet + 1
            a=float(input("Zadej číslo: "))
    print(soucet/(pocet))

#cyklusWhile3()

def cyklusWhile4():
    a=float(input("Zadej číslo: "))
    b=float(input("Zadej druhé číslo: "))
    volba =""
    while(volba!="3."):
        volba=input("Vyber mezi: 1.= soucet, 2.= prumer, 3.= konec:     ")
        if volba =="1.":
            print("součet: " + str(a+b))
        elif volba == "2.":
            print("průměr: " + str((a+b)/2))
        elif volba !="3.":
            print("chybná volba! ")
        else:
            print()

#cyklusWhile4()
                  
def cyklusWhile5():
    a=float(input("Zadej číslo: "))
    b=float(input("Zadej druhé číslo: "))
    volba =""
    while(volba!="3."):
        volba=input("Vyber mezi: 1.= soucet, 2.= prumer, 3.= minimum, 4.= konec:     ")
        if volba =="1.":
            print("součet: " + str(a+b))
        elif volba == "2.":
            print("průměr: " + str((a+b)/2))
        elif volba =="3.":
            if (a<b):
                print("minimum: " + str(a))
            elif (a>b):
                print("minimum: " + str(b))
        elif volba !="4.":
            print("chybna volba! ")
        else:
            print()        
    
#cyklusWhile5():

#Dů
#Načítejte čísla, načítání bude ukončeno, když jejich součet bude > 100,
#Potom se hodnoty vypíšou a zobrazí se i průměrná hodnota


def cyklusWhileDu():
    pocet=0
    soucet=0
    a=0
    hodnoty=""
    a=float(input("Zadej číslo: "))
    while (soucet + a)<101:
        hodnoty= hodnoty + str(a) + "; "
        soucet= soucet + a
        pocet= pocet + 1
        a=float(input("Zadej číslo: "))
    print("průměr: ",soucet/pocet)
    print("hodnoty: ", hodnoty + str(a))

#cyklusWhileDu()


def Len():
    text=input("Zadej text: ")
    print("první znak: ",text[0] + "\n" + "posledni znak: " + str(text[len(text)-1]))

#Len()
    
def WhileLen():
    tisk=""
    text="12"
    while len(text) > 1:
         text= input("Zadej text: ")
         if text[0]!=" " and len(text)>1 :
             tisk = tisk + text + "\n"
    print(tisk)
    
WhileLen()

def cyklusFor():
    for i in "ahoj":
        print(i)
#cyklusFor()

def cyklusFor2():
    for i in range(10):
        print(i)
#cyklusFor2()

def cyklusFor3():
    pocet=int(input("Zadej počet hvězdiček: "))
    for i in range(1, pocet+1):
        print("*")

#cyklusFor3()

def cyklusFor4():
    tisk=""
    for y in range(1,11):
        for i in range(y):
            tisk= tisk + "*"
        print(tisk)
        tisk=""


#cyklusFor4()
    
def cyklusFor5():
    tisk=""
    for y in range(1,11):
        for i in range(11-y):
            tisk= tisk + "*"
        print(tisk)
        tisk=""


#cyklusFor5()

#Zada čísla od 1 do 10 a vypíše to jejich prům hodnotu
def cyklusFor6():
    pocet=0
    soucet=0
    for i in range(1,11):
        soucet= soucet + i
        pocet=pocet+1
        print(i)
    print("průměr: ",soucet/pocet)
    
#cyklusFor6()







                  
