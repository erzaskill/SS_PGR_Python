def funkcefor():
    for y in "ahoj": #vypíše všechny znaky.. každý znak na jednom řádku
        print(y)
#funkcefor()


def vypiscisla():
    for y in range(5, 10, 2): #vypíše číslo od prvního zadaného čísla
                            #až po číslo o jedno méně než je napsané
                            #a pujde to po dvou
                            #for i in range(10): #range(10) 0 do 9
                            #for i in range(1, 10): #range(10) 1 do 9
                            #for i in range(1,11,2): #oblast od 1 do 10 po dvou
        print(y)
#vypiscisla()

def mocnina():
    a= int(input("Zadej horní hranici: ")) #musí tam být int)
    for y in range(1,a+1):
        print(y,"          ",y*y) #místo mezer lze použít tabulátor "\t"
#mocnina()

def pocetcisel():
    soucet=0
    vypis=""
    maxhodnota=-99999999
    minhodnota=9999999
    pocet= int(input("Zadej počet čísel: "))
    for y in range(pocet):
        cislo = float(input("Zadej číslo: "))
        soucet= soucet + cislo
        vypis= vypis + str(cislo) + "; "
        if cislo > maxhodnota:
            maxhodnota=cislo
        if cislo < minhodnota:
            minhodnota=cislo
    print("průměr: ",soucet/pocet)
    print("vypis; ", vypis)
    print("maximum: ",maxhodnota)
    print("minimum: ",minhodnota)
#pocetcisel()


def vypisznaku():
    pocet= int(input("Zadej počet znaků: "))
    vypis=""
    for y in range(pocet):
        vypis= vypis + "*"
    print(vypis)
        

#vypisznaku()

def slovo():
    slovo=input("slovo: ")
    pocet=len(slovo)-1
    vypis=""
    for y in range(pocet):
        vypis= vypis + "*"
    print(slovo[0]+vypis)
#slovo()

