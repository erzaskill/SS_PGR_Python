#While

def ZkousimWhile():
    a=1
    soucet=0
    pocet=0
    while a>0:
        a=float(input("Zadej číslo: "))
        if a>0:    
            soucet= soucet + a
            pocet= pocet + 1
    print("Pruměr: ",soucet/pocet)

#ZkousimWhile()

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

def cyklusWhileOpakuji():
    a=float(input("Zadej první číslo: "))
    b=float(input("Zadej druhé číslo: "))
    vyber=""
    while vyber!="3.":
        vyber=input("Vyber si: 1.=>soucin, 2.=>prumer, 3.=>konec___")
        if vyber == "1.":
            print("součin: ",a*b)
        elif vyber == "2.":
            print("prumer: ",(a+b)/2)
        elif vyber != "3.":
            print("Nevybral sis z uvedených možností nebo si nenapsal tečku")
        elif vyber == "3.":
            print("Vybral sis ukončení cyklu!")
        else:
            ()

cyklusWhileOpakuji()

        



