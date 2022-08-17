#Zadejte text, program zjístí počet mezer v textu

def ForOpk():
    text=input("Zadej text: ")
    pocet=0
    for i in(text):
        if i == " ":
            pocet=pocet+1
    print(pocet)
#ForOpk()
#Program se zeptá kolik hvězdiček chcem vypsat, po zadání počtu vypíše na každém řádku jednu
def ForOpk1():
    tisk=""
    pocet=int(input("Zadej počet znaků: "))
    for i in range(pocet):
        tisk= tisk + "*" + "\n"
    print(tisk)
            
#ForOpk1()

def ForOpk2():
    vypis=""
    soucet=0
    OpacnyVypis=""
    pocet=0
    min=6465465465465
    max=-2554465465465
    otazka=int(input("Kolik čísel chceš načíst? "))
    for i in range(otazka):
        a=float(input("Zadej číslo: "))
        if a<min:
            min=a
        if a>max:
            max=a
        soucet= soucet + a
        pocet= pocet + 1
        vypis= vypis + str(a) + "; "
        OpacnyVypis= str(a) + "; " + OpacnyVypis
    print("Součet: " + str(soucet) + "\n" + "Vypis: " + str(vypis) + "\nOpacny Vypis: " + str(OpacnyVypis) + "\nMinimální hodnota: " + str(min) + "\nMaximální hodnota: " + str(max) + "\nPrůměrná hodnota: " + str(soucet/pocet))
#ForOpk2()



#pro pracování s náhodným číslem, musíme napsat do konzole import random.. (příkaz krerý slouží k vygenerování náhodných čísel v nějakem rozsauhu od, do je: random.randint(a,b)

import random
#program se zeprá na počet čísel
#pak vygeneruje zadaný počet náhodných čísel
#čísla vypíše na řádku odděleně. (poslední středník odebereme)


def Nahodnacisla():
    a=int(input("Kolik čísel se má vygenerovat? :"))
    tisk=""
    for i in range(a):
        tisk=tisk + str(random.randint(-100,100)) + " ;"
    print(tisk[0:(len(tisk))-1])#jde to i jednodušeji: print(tisk[0:-2])

#Nahodnacisla()


    
#vypíše navíc průměrnou hodnotu
def Nahodnacisla1():
    a=int(input("Kolik čísel se má vygenerovat? :"))
    soucet=0
    tisk=""
    cislo= 0
    max=-654564654
    min=65456465
    for i in range(a):
        cislo= random.randint(-100,100)
        soucet= soucet + cislo
        tisk=tisk + str(cislo) + " ;"
        if cislo>max:
            max=cislo
        elif cislo<min:
            min=cislo
    print(tisk[0:(len(tisk))-1] + "\nprůměr: " + str(soucet/a) + "\nmaximální hodnota: " + str(max) + "\nminimální hodnota: " + str(min))#jde to i jednodušeji: print(tisk[0:-2])
    print(len(tisk))
#Nahodnacisla1()



    
#simulace hry "KOSTKY"
def Nahodnacisla2():
    pocet = int(input("Počet hodů: "))
    vyhraPC= 0
    vyhraClovek= 0
    for i in range(pocet):
        hClovek= random.randint(1,6)
        hPC= random.randint(1,6)
        print("hod č.", i+1)
        print("PC: ",hPC)
        print("Ty jsi hodil: ", hClovek)

        if hClovek > hPC:
            print("Vyhral jsi!!")
            vyhraClovek = vyhraClovek + 1
        
        elif hClovek < hPC:
            print("Prohral jsi!!!")
            vyhraPC=vyhraPC + 1
        
        else: print ("Je to nerozhodně")
        input("Pokračuj!")
        print("\n\n")
    if vyhraClovek < vyhraPC:
        print("Prohrál si celou hru!")
    elif vyhraClovek > vyhraPC:
        print("Vyhral si celou hru!")
    else:
        print("Hra zkončila nerozhodně!")
    

#Nahodnacisla2()

#TEST n a cyklus FOR příští hodinu
        
    














































