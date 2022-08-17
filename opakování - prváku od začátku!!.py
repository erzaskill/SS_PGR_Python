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
    type(a)
#maxprum()

def cyklusWhile():
    a=1
    soucet= 0
    pocet= 0
    while (a!=0): #a!=0 znamená různé od nuly
        a=float(input("Zadej číslo: "))
        soucet= soucet + a
        pocet= pocet + 1
    print("průměr: ",soucet/(pocet-1))

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
    print("průměr: ",soucet/(pocet))

#cyklusWhile2()

def cyklusWhile3():
    a=2
    soucet= 0
    pocet= 0
    a=float(input("Zadej číslo: "))
    while (a>0): #a!=0 znamená různé od nuly         
            soucet= soucet + a
            pocet= pocet + 1
            a=float(input("Zadej číslo: "))
    print("průměr: ",soucet/(pocet))

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
    while(volba!="4."):
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
            print("chybná volba! ")
        elif volba =="4.":
            print("Konec cyklu")
        else:
            print()
            

#cyklusWhile5()






#Načti dvě čísla a udělej jejich součet a průměr do doby dokud se součet + průměr nebude vyšší nebo stejný jak 30


def ZkousimWhile():

    soucet=0
    prumer=0
    while (soucet+prumer)<30:
        a=float(input("Zadej první číslo: "))
        b=float(input("Zadej druhé číslo: "))
        soucet=  (a+b)   
        prumer= ((a+b)/2)
    print("Součet + průměr je vyšší než 29")
ZkousimWhile()
































            




                      
