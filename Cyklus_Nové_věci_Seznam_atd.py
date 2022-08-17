#proměnná má více hodnot.. Dávají se do seznamu..
def seznam():
    cisla = []
    cisla.append(2)
    cisla.append(3)
    cisla.append(100)
    print(cisla)
#seznam()
#Vytvoření seznamu
import random

def seznamVytvoreni():
    cisla=[]
    for i in range(10):
        cisla.append(random.randint(-10,10))
    print(cisla)
#seznamVytvoreni()

#program vygeneruj n cisel do seznamu
#vypíše všechny kladné hodnoty ze seznamu
def seznamKladnaCisla():
    cisla=[]
    pocet=int(input("pocet: "))
    for i in range(pocet):
        cisla.append(random.randint(-10,10))
    print(cisla)
    tisk=""
    tiskOpak=""
    for i in range(len(cisla)):
        if cisla[i]>0:
            tisk=tisk + str(cisla[i]) + "; "
            tiskOpak= str(cisla[i]) + "; " + tiskOpak
    print("Kladné hodnoty: " + str(tisk) + "\nOpačný výpis: " + str(tiskOpak))

#seznamKladnaCisla()

def seznamFunkce():
    cisla=[]
    pocet= 3
    for i in range(pocet):
        cisla.append(random.randint(1,10))
    print("seznam: ", cisla)

    soucet = sum(cisla)
    prumer = soucet/len(cisla)

    print("soucet",soucet)
    print("průměr: ",prumer)
    print("max: ", max(cisla))
    print("min: ", min(cisla))
    cisla.sort() # seřadí čísla(prvky)
    print("seřadit: ", cisla)
    cisla.sort(reverse=True) #seřadí prvky opačně, sestupně
    print("seřadit opačně: ", cisla)

#seznamFunkce()




def seznamFunkce1():
    texty=[]
    pocet= 3
    for i in range(pocet):
        texty.append("Ahoj")
        texty.append("Čau")
        texty.append("Velbloud")
    print("seznam: ", texty)

    soucet = sum(texty)
    prumer = soucet/len(texty)

    print("soucet",soucet)
    print("průměr: ",prumer)
    print("max: ", max(texty))
    print("min: ", min(texty))
    cisla.sort() # seřadí čísla(prvky)
    print("seřadit: ", texty)
    cisla.sort(reverse=True) #seřadí prvky opačně, sestupně
    print("seřadit opačně: ", texty)
####Nefunguje.. Zkontrolovat!!!
    
#seznamFunkce1()
    
#Vypíše všechny dny
    
def nahodneDny():
    dny=["Po","ut","str","ct","pa","so","ne"]

    for i in range(7):
        print(dny[i])
#nahodneDny()

import random
def nahodneMesiceDny():
    dny=["Po","ut","str","ct","pa","so","ne"]
    mesice=["Leden","Únor","Březen","Duben","Květen","Červen","Červenec"]
    mesice= mesice + ["Srpen","Září","Říjen","Listopad","Prosinec"]
    v=""
    for i in range(10):
        a=random.randint(0,6)
        b=random.randint(0,11)
        v= mesice[b] + " " + dny[a]
        if a == 6 or a==5:
            v="!!!!"+v+"!!!!"
        if b<6:
            v="První pololetí " + v
        elif b>5:
            v="Druhé pololetí " + v
        else:
            print(v)
        print(v)   

#nahodneMesiceDny()


def seznam1():
    pocet=int(input("pocet: "))
    lide=[]
    for i in range (pocet):
        lide.append(input("Zadej příjmení a jméno oddelene _: "))
    lide.sort()
    print(lide)
#seznam1()

def email():
    pocet=int(input("pocet: "))
    lide=[]
    for i in range (pocet):
        lide.append(input("Zadej příjmení a jméno oddelene _: "))
    lide.sort()

    #vytvoření mail. adresy a vložení do seznamu mail
    mail=[]
    for i in range(pocet):
        mail.append(lide[i]+"@gmail.com")

    #výpis: jméno a mailová adresa
    for i in range(pocet):
        print(lide[i], mail[i])

#email()


#vytvořte seznam-cisla1 a vygenerujte do něj n čísel
#vytvořte seznam2 - bude obsahovat hodnoty ze seznamu, zvětšené o 10
#oba seznamy vytiskněte

def seznam2():
    cisla1=[]
    pocet=10
    for i in range(pocet):
        cisla1.append(random.randint(1,11))
    cisla1.sort

    zvetsene=[]
    for i in range(pocet):
        zvetsene.append(cisla1[i]+10)
    zvetsene.sort

    for i in range(pocet):
        print(cisla1[i], zvetsene[i])


#seznam2()


#Program bude načítat jména pracovníků (příjmení + mezera + křestná)
#Bude je ukládast do seznamu.
#Po načtení dá možnosti: 1. Výpis, 2. Výpis seřazený vzestupně


def pracovnici():
    pracovnici=[]
    pocet=int(input("Zadej počet pracovníků: "))
    volba=""
    for i in range(pocet):
    
        pracovnici.append(input("Zadej prijmeni + jméno: "))

    volba=input("Zadej svou volbu (1=výpis, 2.výpis seřazený vzestupně): ")
    if volba=="1":
        for i in range(pocet):
            print(pracovnici[i])

    elif volba=="2":
        for i in range(pocet):
            pracovnici.sort
            print(pracovnici[i])

#pracovnici()

#To samé v cyklu po zadání 3.. se program ukončí jinak se načítá pořád dokola

def pracovniciWhile():
    pracovnici=[]
    pocet=int(input("Zadej počet pracovníků: "))
    for i in range(pocet):
    
        pracovnici.append(input("Zadej prijmeni + jméno: "))
    pracovniciR = pracovnici[:] #takhle se dělá kopie seznamu
    volba=""    
    while (volba!=4):
        volba=input("Zadej svou volbu (1=výpis, 2.výpis seřazený vzestupně, 3.vložení jména, 4.konec programu): ")
        if volba=="1":
            for i in range(len(pracovnici)):
                print(pracovnici[i])

        elif volba=="2":
            pracovniciR.sort() #se závorkou se to seřadí abecedně, bez závorky podle pořadí zadání(využijeme kopii seznamu aby to seřadilo kopii a pak to nebylop seřazené na vždy
            for i in range(len(pracovniciR)):
                
                print(pracovniciR[i])

        elif volba=="3":
            for i in range(1):
                jmeno = input("Zadej prijmeni + jmeno: ")
                pracovnici.append(jmeno)
                pracovniciR.append(jmeno)
                

        elif volba!="4":
            print("Napsal si to špatně, nebo sis nevybral možnost z volby")

        else:
            break
               

pracovniciWhile()


def FunkceSplit(): #funkce která nám z daného textu rozdělí text do seznamu.. Z věty nám vypíše jednotlivá slova v seznamu.. po každé mezeře jedno slovo v textu
    text= input ("Napiš větu: ")
    seznam = text.split()
    print(seznam)
#FunkceSplit()

#Zkus seřadit text vzestupně sestupně.. najdi nekratší a nejdelší slovo...
    
        






    
    
